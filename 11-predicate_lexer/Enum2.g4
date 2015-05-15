grammar Enum2;
@lexer::members {_java5 = False}

prog:   (   stat 
        |   enumDecl
        )+
    ;

stat:   ID '=' expr ';' {print($ID.text+"="+$expr.text)} ;

expr:   ID
    |   INT
    ;

// No predicate needed here because 'enum' token undefined if !java5
enumDecl
    :   'enum' name=ID '{' ID (',' ID)* '}'
        {print("enum "+$name.text)}
    ;

ENUM:   'enum' {self._java5}? ; // must be before ID
ID  :   [a-zA-Z]+ ;


INT :   [0-9]+ ;
WS  :   [ \t\r\n]+ -> skip ;
