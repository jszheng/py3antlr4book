# The build-in Error report

% antlr4py3 Simple.g4
% pygrun Simple prog in1.txt
var i
class T

% pygrun Simple prog in2.txt
line 2:19 mismatched input '4' expecting ';'
method: f
class T

% pygrun Simple prog in3.txt
line 1:7 extraneous input ';' expecting '{'
var i
class T

% pygrun Simple prog in4.txt
found assign: a=3;
method: f
line 2:21 missing '}' at '<EOF>'
class T

% pygrun Simple prog in5.txt
line 1:14 no viable alternative at input 'int;'
class T

% pygrun Simple prog in6.txt
line 1:6 token recognition error at: '#'
line 1:8 missing ID at '{'
var i
class <missing ID>

# Verbose Listener

% python TestE_Listener.py in7.txt
rule stack:  ['prog', 'classDef']
line 1 : 8 at [@2,8:8='T',<10>,1:8] : extraneous input 'T' expecting '{'
rule stack:  ['prog', 'classDef', 'member']
line 2 : 6 at [@5,19:19=';',<5>,2:6] : no viable alternative at input 'int;'
class T 