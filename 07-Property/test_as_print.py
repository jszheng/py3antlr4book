import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from PropertyFileLexer import PropertyFileLexer
from PropertyFileParser import PropertyFileParser


class PropertyFilePrinter(PropertyFileParser):
    def defineProperty(self, name, value):
        print(name.text, ' = ', value.text)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = PropertyFileLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PropertyFilePrinter(token_stream)
    parser.top()
