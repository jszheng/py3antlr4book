__author__ = 'jszheng'

from ExprListener import ExprListener


class MyListener(ExprListener):
    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx):
        print('EnterProg')

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx):
        print('ExitProg')


    # Enter a parse tree produced by ExprParser#stat.
    def enterStat(self, ctx):
        print('EnterStat')

    # Exit a parse tree produced by ExprParser#stat.
    def exitStat(self, ctx):
        print('ExitStat')


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx):
        print('EnterExpr')

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx):
        print('ExitExpr')


