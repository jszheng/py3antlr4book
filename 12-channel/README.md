# Shift Comment to top
There is no TokenStreamRewriter in the python runtime. It does not have to. if you dive into the source code, the CommonTokenStream is derived from BufferedTokenStream which has a list of CommonToken. It is re-writable. 

in the listener
```python
class CommentShifter(CymbolListener):
    def __init__(self, tokens:CommonTokenStream):
        super().__init__()
        self.tokens = tokens  # record the token stream from parser

    def exitVarDecl(self, ctx:CymbolParser.VarDeclContext):
        startIndex = ctx.start.tokenIndex
        stopIndex = ctx.stop.tokenIndex
        cmtChannel = self.tokens.getHiddenTokensToRight(stopIndex, CymbolLexer.COMMENTS)
        if cmtChannel != None:
            tok = cmtChannel[0]
            if tok != None:  # find out a comment followed, it is one token
                # self.tokens is CommonTokenStream
                # self.tokens.tokens is the list of CommonToken
                token_array = self.tokens.tokens
                token_array.insert(startIndex, tok.clone())
                tok.text = "\n"
```

# How to run
```
% python shift_var_comments.py t.cym
(startrule 
  (varDecl (datatype int) n = (expr 0) ;) 
  (varDecl (datatype int) i = (expr 9) ;)
)
// define a counter
int n = 0;
int i = 9;
```