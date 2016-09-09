grammar Simple;

prog:   classDef+ ; // match one or more class definitions

classDef
    :   'class' ID '{' member+ '}' // a class has one or more members
        {print("class "+$ID.text);}
    ;

member
    :   'int' ID ';'                       // field definition
        {print("var "+$ID.text);}
    |   'int' f=ID '(' ID ')' '{' stat '}' // method definition
        {print("method: "+$f.text);}
    ;

stat:   expr ';'
        {print("found expr: " + $text);}
    |   ID '=' expr ';'
        {print("found assign: " + $text);}
    ;

expr:   INT 
    |   ID '(' INT ')'
    ;

INT :   [0-9]+ ;
ID  :   [a-zA-Z]+ ;
WS  :   [ \t\r\n]+ -> skip ;

