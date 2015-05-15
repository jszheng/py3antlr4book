
import sys
from antlr4 import *
from antlr4 import InputStream

from CSVLexer import CSVLexer
from CSVParser import CSVParser

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = CSVLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CSVParser(token_stream)
    parser.buildParseTrees = False
    parser.start()