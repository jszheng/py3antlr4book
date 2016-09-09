import sys
from antlr4 import *
from antlr4.error.ErrorListener import *
from pprint import pprint

from SimpleLexer import SimpleLexer
from SimpleParser import SimpleParser



class VerboseListener(ErrorListener) :
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("rule stack: ", str(stack))
        print("line", line, ":", column, "at", offendingSymbol, ":", msg)


def main(argv):
    istream = FileStream(argv[1])
    lexer = SimpleLexer(istream)
    stream = CommonTokenStream(lexer)
    parser = SimpleParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(VerboseListener())
    parser.prog()


if __name__ == '__main__':
    main(sys.argv)
