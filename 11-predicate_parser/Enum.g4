grammar Enum;
@parser::init {}
@parser::members {_java5 = False}

prog:   (   stat 
        |   enumDecl
        )+
    ;

stat:   identifier '=' expr ';' {print($identifier.text+"="+$expr.text)} ;

expr
    :   identifier
    |   INT
    ;

enumDecl
    :   {self._java5}? 'enum' name=identifier '{' identifier (',' identifier)* '}'
        {print("enum "+$name.text)}
    ;

identifier  :   ID
    |   {not self._java5}? 'enum'
    ;
    
ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;
WS  :   [ \t\r\n]+ -> skip ;
