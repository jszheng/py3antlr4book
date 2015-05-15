Predicate in Lexer

```
When you set Enum2Lexer._java5 = True
% python test_EnumLexer.py Temp.java
enum Temp

When you set Enum2Lexer._java5 = False
% python test_EnumLexer.py Temp.java
line 1:5 missing '=' at 'Temp'
line 1:15 mismatched input ',' expecting '='
line 1:22 mismatched input '}' expecting '='
```