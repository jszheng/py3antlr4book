Predicate in Parser

```
% antlr4py3 Enum.g4

Set EnumParser._java5 = True
% python test_EnumParser.py Temp.java
enum Temp

Set EnumParser._java5 = False
% python test_EnumParser.py Temp.java
line 1:0 no viable alternative at input 'enum'
```
