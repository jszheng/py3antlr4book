__author__ = 'jszheng'
"""
Using Listener, store data in stack. result at the top of the stack
"""

import sys
from antlr4 import *
from antlr4.InputStream import InputStream


from LExprLexer import LExprLexer
from LExprParser import  LExprParser
from LExprListener import LExprListener


class EvalListener(LExprListener):
    def __init__(self):
        self.stack = []

    def exitMult(self, ctx):
        right = self.stack.pop()
        left  = self.stack.pop()
        self.stack.append(right * left)

    def exitAdd(self, ctx):
        right = self.stack.pop()
        left  = self.stack.pop()
        self.stack.append(right + left)

    def exitInt(self, ctx):
        self.stack.append(int(ctx.INT().getText()))


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
    listener = EvalListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print('result_stack=', listener.stack)
