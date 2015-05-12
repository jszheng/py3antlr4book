import sys
from antlr4 import *
from ArrayInitLexer import ArrayInitLexer
from ArrayInitParser import ArrayInitParser
from rewriter import RewriteListener

def main(argv):
    istream = FileStream(argv[1])
    lexer = ArrayInitLexer(istream)
    stream = CommonTokenStream(lexer)
    parser = ArrayInitParser(stream)
    tree = parser.init()
    print(tree.toStringTree(recog=parser))

    walker = ParseTreeWalker()
    walker.walk(RewriteListener(), tree)
    print()

if __name__ == '__main__':
    main(sys.argv)
