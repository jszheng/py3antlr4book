# Cymbol
Two example here
- Generate call graph
- Check variable 

# How to run
```
% antlr4py3 Cymbol.g4
% python CallGraph.py t.cymbol

digraph G {
  ranksep=.25;
  edge [arrowsize=.5]
  node [shape=circle, fontname="ArialNarrow",
        fontsize=12, fixedsize=true, height=.45];

  main;fact;a;b;c;d;e;
  main -> fact;
  main -> a;
  fact -> print;
  fact -> fact;
  a -> b;
  a -> c;
  a -> d;
  b -> c;
  c -> b;

}

% python CheckSymbols.py vars.cymbol
*** Scan Definitions ***
locals : []
function <f:INT> : <y:FLOAT>;<x:INT>;
locals : ['y', 'x']
function <g:VOID> :
globals : ['g', 'f']

*** Check errors ***
[Error] line 3:4 no such variable: i
[Error] line 4:4 g is not a variable
[Error] line 13:4 no such function: z
[Error] line 14:4 y is not a function
[Error] line 15:8 f is not a variable

% python CheckSymbols.py vars2.cymbol
*** Scan Definitions ***
locals : ['y']
locals : ['x']
function <a:VOID> :
locals : []
function <b:VOID> : <z:INT>;
globals : ['b', 'y', 'x', 'a']

*** Check errors ***

```