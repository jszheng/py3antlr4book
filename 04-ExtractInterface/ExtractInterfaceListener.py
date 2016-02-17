__author__ = 'jszheng'

from antlr4 import *
from JavaListener import JavaListener
from JavaParser import JavaParser


class ExtractInterfaceListener(JavaListener):

    # need parser to extract token stream
    def __init__(self, parser: JavaParser):
        self.parser = parser

    # Enter a parse tree produced by JavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx):
        print('interface I', ctx.Identifier(), ' {', sep='')

    # Exit a parse tree produced by JavaParser#classDeclaration.
    def exitClassDeclaration(self, ctx):
        print('}')

    # should the function becomes function of Rule Context?
    def getAllText(self, ctx):  # include hidden channel
        token_stream = ctx.parser.getTokenStream()
        lexer = token_stream.tokenSource
        input_stream = lexer.inputStream
        start = ctx.start.start
        stop = ctx.stop.stop
        return input_stream.getText(start, stop)

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):

        dt = 'void'  # extract data type string, None means void
        dt_ctx = ctx.datatype()
        if dt_ctx is not None:
            dt = self.getAllText(dt_ctx)
        args = self.getAllText(ctx.formalParameters())
        print("\t", dt, ' ', ctx.Identifier(), args, ';', sep='')