__author__ = 'jszheng'

import sys
from antlr4 import *
from Enum2Lexer import Enum2Lexer
from Enum2Parser import Enum2Parser

if __name__ == '__main__':
    Enum2Lexer._java5 = True

    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = Enum2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Enum2Parser(token_stream)
    parser.buildParseTrees = False
    parser.prog()