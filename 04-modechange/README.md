# How to run
```
% python test.py t.xml
0 8 3 413 413 4 \n
0 9 0 414 414 1 <
0 9 1 415 419 10 tools
0 9 6 420 420 5 >
0 9 7 421 422 4 \n\t
0 10 1 423 423 1 <
0 10 2 424 427 10 tool
0 10 7 429 432 10 name
0 10 11 433 433 7 =
0 10 12 434 440 8 "ANTLR"
0 10 19 441 441 5 >
0 10 20 442 459 4 A parser generator
0 10 38 460 460 1 <
0 10 39 461 465 9 /tool
0 10 44 466 466 5 >
0 10 45 467 467 4 \n
0 11 0 468 468 1 <
0 11 1 469 474 9 /tools
0 11 7 475 475 5 >
0 11 8 476 476 4 \n
```

# What's in this test
- Lexer Only, call nextToken() method till end of file (Token.EOF)
- Switch Mode
