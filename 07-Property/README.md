# Property Parsing
- Using Listener/Visitor
- Call back inserted in action

# How to run
```
% antlr4py3 -visitor PropertyFile.g4

% python test_listener.py t.properties
user => "parrt"
machine => "maniac"

% python test_visitor.py t.properties
machine => "maniac"
user => "parrt"

% python test_as_print.py t.properties
user  =  "parrt"
machine  =  "maniac"

% python test_as_loader.py t.properties
machine => "maniac"
user => "parrt"
```