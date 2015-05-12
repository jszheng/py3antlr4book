from ArrayInitListener import ArrayInitListener


class RewriteListener(ArrayInitListener):
    # Enter a parse tree produced by ArrayInitParser#init.
    def enterInit(self, ctx):
        print("\"", end='')

    # Exit a parse tree produced by ArrayInitParser#init.
    def exitInit(self, ctx):
        print("\"", end='')

    # Enter a parse tree produced by ArrayInitParser#value.
    def enterValue(self, ctx):
        pass

    # Exit a parse tree produced by ArrayInitParser#value.
    def exitValue(self, ctx):
        data = ctx.INT().getText()
        print('\\u%04x' % int(data), end='')