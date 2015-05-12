__author__ = 'jszheng'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from MyVisitor import MyVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = LabeledExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LabeledExprParser(token_stream)
    tree = parser.prog()

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    visitor = MyVisitor()
    visitor.visit(tree)
