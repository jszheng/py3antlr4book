__author__ = 'jszheng'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from RowsLexer import RowsLexer
from RowsParser import RowsParser

if __name__ == '__main__':
    if len(sys.argv) > 1:
        col_num = int(sys.argv[1])
        input_stream = FileStream(sys.argv[2])
    else:
        print('Usage: python col.py #col file')
        exit(1)

    lexer = RowsLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RowsParser(token_stream)
    parser.column = col_num
    parser.buildParseTrees = False
    tree = parser.rows()