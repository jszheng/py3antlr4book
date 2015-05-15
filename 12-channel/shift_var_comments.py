__author__ = 'jszheng'

import sys
from antlr4 import *
from antlr4 import InputStream

from CymbolLexer import CymbolLexer
from CymbolParser import CymbolParser
from CymbolListener import CymbolListener


class CommentShifter(CymbolListener):
    def __init__(self, tokens:CommonTokenStream):
        super().__init__()
        self.tokens = tokens

    def exitVarDecl(self, ctx:CymbolParser.VarDeclContext):
        startIndex = ctx.start.tokenIndex
        stopIndex = ctx.stop.tokenIndex
        cmtChannel = self.tokens.getHiddenTokensToRight(stopIndex, CymbolLexer.COMMENTS)
        if cmtChannel != None:
            tok = cmtChannel[0]
            if tok != None:
                token_array = self.tokens.tokens
                token_array.insert(startIndex, tok.clone())
                tok.text = "\n"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = CymbolLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CymbolParser(token_stream)
    tree = parser.startrule()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    walker = ParseTreeWalker()
    collector = CommentShifter(token_stream)
    walker.walk(collector, tree)
    print(token_stream.getText())
