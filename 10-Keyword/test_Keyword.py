__author__ = 'jszheng'

import sys
from antlr4 import *
from antlr4 import InputStream
from KeywordsLexer import KeywordsLexer
from KeywordsParser import KeywordsParser

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = KeywordsLexer(input_stream)
    # there is no way to insert code in the __init__ function
    # from ANTLR file. just hack here, or could just create new class
    setattr(lexer, 'keywords', {
        'begin': KeywordsParser.BEGIN,
        'if':    KeywordsParser.IF,
        'then':  KeywordsParser.THEN,
        'while': KeywordsParser.WHILE
    })

    # tk = lexer.nextToken()
    # while tk.type != Token.EOF:
    #     print(tk)
    #     tk = lexer.nextToken()

    token_stream = CommonTokenStream(lexer)
    parser = KeywordsParser(token_stream)
    parser.stat()
