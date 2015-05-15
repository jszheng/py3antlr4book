import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from PropertyFileLexer import PropertyFileLexer
from PropertyFileParser import PropertyFileParser


class PropertyFileLoader(PropertyFileParser):
    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.props = {}

    def defineProperty(self, name, value):
        self.props[name.text] = value.text

    def show(self):
        for (key, value) in self.props.items():
            print(key, '=>', value)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = PropertyFileLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PropertyFileLoader(token_stream)
    parser.top()
    parser.show()