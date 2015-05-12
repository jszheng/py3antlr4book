# Calculator
This example shows
- Visitor Pattern
- Use of Alternative Label

# How to run
```
% antlr4py3 -visitor -no-listener LabeledExpr.g4
% type t.expr
193
a = 5
b = 6
a+b*2
(1+2)*3

% python calc.py t.expr
193
17
9
```