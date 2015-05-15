__author__ = 'jszheng'
import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from DataLexer import DataLexer
from DataParser import DataParser

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = DataLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DataParser(token_stream)
    tree = parser.top()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)