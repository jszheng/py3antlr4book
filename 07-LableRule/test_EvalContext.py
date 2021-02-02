__author__ = 'jszheng'
"""
To Store value with the context associated to the tree
"""


import sys
from antlr4 import *
from antlr4.InputStream import InputStream


from LExprLexer import LExprLexer
from LExprParser import  LExprParser
from LExprListener import LExprListener


class ContextMap(LExprListener):
    def exitInt(self, ctx):
        ctx.value = int(ctx.INT().getText())

    def exitAdd(self, ctx):
        left = ctx.e(0).value
        right= ctx.e(1).value
        ctx.value = left + right

    def exitMult(self, ctx):
        left = ctx.e(0).value
        right= ctx.e(1).value
        ctx.value = left * right

    def exitS(self, ctx):
        ctx.value = ctx.e().value


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = LExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LExprParser(token_stream)
    tree = parser.s()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    # listener
    print("Start Walking...")
    listener = ContextMap()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print('result_at_top =', listener.value)
