__author__ = 'jszheng'


import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from CSVLexer import CSVLexer
from CSVParser import CSVParser
from CSVListener import CSVListener


class CsvLoader(CSVListener):
    def __init__(self):
        self.rows = []
        self.header = []
        self.current = []

    def exitString(self, ctx):
        self.current.append(ctx.STRING().getText())

    def exitText(self, ctx):
        self.current.append(ctx.TEXT().getText())

    def exitEmpty(self, ctx):
        self.current.append('')

    def exitHdr(self, ctx):
        self.header = self.current

    def enterRow(self, ctx):
        self.current = []

    def exitRow(self, ctx):
        # getParent() method does not exist, use 'parentCtx' field here.
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_hdr:
            return
        m = dict(zip(self.header, self.current))
        self.rows.append(m)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = CSVLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CSVParser(token_stream)
    tree = parser.top()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    # listener
    print("Start Walking...")
    listener = CsvLoader()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print('result =', listener.rows)
