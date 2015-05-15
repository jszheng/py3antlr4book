__author__ = 'jszheng'

import sys

from antlr4 import *
from antlr4.InputStream import InputStream
from SymbolScope import *

from CymbolLexer import CymbolLexer
from CymbolParser import CymbolParser
from CymbolListener import CymbolListener


def get_type(tokenType):
    if tokenType == CymbolParser.K_FLOAT:
        return Symbol.TypeEnum.FLOAT
    elif tokenType == CymbolParser.K_INT:
        return Symbol.TypeEnum.INT
    elif tokenType == CymbolParser.K_VOID:
        return Symbol.TypeEnum.VOID
    else:
        return Symbol.TypeEnum.INVALID


def error(token, msg):
    print('[Error] line %d:%d %s' % (token.line, token.column, msg))


class DefPhase(CymbolListener):
    def __init__(self):
        self.globals = None
        self.currentScope = None
        self.scopes = {}
        pass

    def enterTop(self, ctx):
        self.globals = GlobalScope(None)
        self.currentScope = self.globals

    def exitTop(self, ctx):
        print(self.globals)

    def enterFunctionDecl(self, ctx: CymbolParser.FunctionDeclContext):
        name = ctx.ID().getText()
        stoken_type = ctx.primtype().start.type
        stype = get_type(stoken_type)
        #
        function = FunctionSymbol(name, stype, self.currentScope)
        self.currentScope.define(function)
        self.scopes[ctx] = function
        self.currentScope = function

    def exitFunctionDecl(self, ctx):
        print(self.currentScope)
        self.currentScope = self.currentScope.getEnclosingScope()

    def enterBlock(self, ctx):
        self.currentScope = LocalScope(self.currentScope)
        self.scopes[ctx] = self.currentScope

    def exitBlock(self, ctx):
        print(self.currentScope)
        self.currentScope = self.currentScope.getEnclosingScope()

    def exitFormalParameter(self, ctx: CymbolParser.FormalParameterContext):
        stoken_type = ctx.primtype().start.type
        stype =get_type(stoken_type)
        var = VariableSymbol(ctx.ID().getText(), stype)
        self.currentScope.define(var)

    def exitVarDecl(self, ctx):
        stoken_type = ctx.primtype().start.type
        stype =get_type(stoken_type)
        var = VariableSymbol(ctx.ID().getText(), stype)
        self.currentScope.define(var)


class RefPhase(CymbolListener):
    def __init__(self, glbs, scopes):
        self.globals = glbs
        self.scopes = scopes
        self.currentScope = None

    def enterTop(self, ctx):
        self.currentScope = self.globals

    def enterFunctionDecl(self, ctx):
        self.currentScope = self.scopes[ctx]

    def exitFunctionDecl(self, ctx):
        self.currentScope = self.currentScope.getEnclosingScope()

    def enterBlock(self, ctx):
        self.currentScope = self.scopes[ctx]

    def exitBlock(self, ctx):
        self.currentScope = self.currentScope.getEnclosingScope()

    def exitVar(self, ctx: CymbolParser.VarContext):
        name = ctx.ID().getText()
        var = self.currentScope.resolve(name)
        if var is None:
            error(ctx.ID().getSymbol(), "no such variable: "+name)
        if isinstance(var, FunctionSymbol):
            error(ctx.ID().getSymbol(), name+" is not a variable")

    def exitCall(self, ctx: CymbolParser.CallContext):
        funcname = ctx.ID().getText()
        meth = self.currentScope.resolve(funcname)
        if meth is None:
            error(ctx.ID().getSymbol(), "no such function: "+funcname)
        if isinstance(meth, VariableSymbol):
            error(ctx.ID().getSymbol(), funcname+" is not a function")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = CymbolLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CymbolParser(token_stream)
    tree = parser.top()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    walker = ParseTreeWalker()

    # definition phase, collect data
    print('*** Scan Definitions ***')
    def_phase = DefPhase()
    walker.walk(def_phase, tree)

    print()

    # reference phase, check error
    print('*** Check errors ***')
    ref_phase = RefPhase(def_phase.globals, def_phase.scopes)
    walker.walk(ref_phase, tree)