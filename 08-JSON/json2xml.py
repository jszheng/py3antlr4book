__author__ = 'jszheng'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from JSONLexer import JSONLexer
from JSONParser import JSONParser
from JSONListener import JSONListener


class XmlEmitter(JSONListener):
    def __init__(self):
        self.xml = {}

    def getXML(self, ctx):
        return self.xml[ctx]

    def setXML(self, ctx, value):
        self.xml[ctx] = value

    def exitAtom(self, ctx):
        self.setXML(ctx, ctx.getText())

    def exitString(self, ctx):
        self.setXML(ctx, ctx.getText().strip('"'))

    def exitObjectValue(self, ctx: JSONParser.ObjectValueContext):
        self.setXML(ctx, self.getXML(ctx.obj()))

    def exitPair(self, ctx: JSONParser.PairContext):
        tag = ctx.STRING().getText().strip('"')
        val = self.getXML(ctx.value())
        x = '<%s>%s</%s>\n' % (tag, val, tag)
        self.setXML(ctx, x)

    def exitAnObject(self, ctx: JSONParser.AnObjectContext):
        buf = "\n"
        for pctx in ctx.pair():
            buf += self.getXML(pctx)
        self.setXML(ctx, buf)

    def exitArrayOfValues(self, ctx: JSONParser.ArrayOfValuesContext):
        buf = "\n"
        for vctx in ctx.value():
            buf += "<element>"
            buf += self.getXML(vctx)
            buf += "</element>\n"
        self.setXML(ctx, buf)

    def exitArrayValue(self, ctx: JSONParser.ArrayValueContext):
        self.setXML(ctx, self.getXML(ctx.array()))

    def exitEmptyArray(self, ctx: JSONParser.EmptyArrayContext):
        self.setXML(ctx, "")

    def exitJson(self, ctx: JSONParser.JsonContext):
        self.setXML(ctx, self.getXML(ctx.getChild(0)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = JSONLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = JSONParser(token_stream)
    tree = parser.json()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    # listener
    print("Start Walking...")
    listener = XmlEmitter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print(listener.getXML(tree))

