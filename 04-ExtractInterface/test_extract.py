__author__ = 'jszheng'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from JavaLexer import JavaLexer
from JavaParser import JavaParser

from ExtractInterfaceListener import ExtractInterfaceListener

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = JavaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParser(token_stream)
    tree = parser.compilationUnit()

    listener = ExtractInterfaceListener(parser)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)



