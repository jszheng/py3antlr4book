__author__ = 'jszheng'

import sys

from antlr4 import *
from antlr4.InputStream import InputStream
from XMLLexer import XMLLexer

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = XMLLexer(input_stream)

    t = lexer.nextToken()
    while t.type != Token.EOF:
        txt = t.text
        if txt is not None:
            txt = txt.replace("\n","\\n")
            txt = txt.replace("\r","\\r")
            txt = txt.replace("\t","\\t")
        else:
            txt = "<no text>"
        print(t.channel, t.line, t.column, t.start, t.stop, t.type, txt)
        t = lexer.nextToken()
