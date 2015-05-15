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
    def __init__(self):
        self.tree_property = {}

    def getValue(self, node):
        return self.tree_property[node]

    def setValue(self, node, value):
        self.tree_property[node] = value

    def exitInt(self, ctx):
        self.setValue(ctx, int(ctx.INT().getText()))

    def exitAdd(self, ctx):
        left = self.getValue(ctx.e(0))
        right= self.getValue(ctx.e(1))
        self.setValue(ctx, left+right)

    def exitMult(self, ctx):
        left = self.getValue(ctx.e(0))
        right= self.getValue(ctx.e(1))
        self.setValue(ctx, left*right)

    def exitS(self, ctx):
        self.setValue(ctx, self.getValue(ctx.e()))


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
    print('result_at_top =', listener.getValue(tree))
