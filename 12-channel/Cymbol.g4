/** Simple statically-typed programming language with functions and variables
 *  taken from "Language Implementation Patterns" book.
 */
grammar Cymbol;

@lexer::members {
WHITESPACE = 1
COMMENTS = 2
}

startrule:   (functionDecl | varDecl)+ ;

varDecl
    :   datatype ID ('=' expr)? ';'
    ;
datatype:   'float' | 'int' | 'void' ; // user-defined types

functionDecl
    :   datatype ID '(' formalParameters? ')' block // "void f(int x) {...}"
    ;

formalParameters
    :   formalParameter (',' formalParameter)*
    ;
formalParameter
    :   datatype ID
    ;

block:  '{' stat* '}' ;   // possibly empty statement block

stat:   block
    |   varDecl
    |   'if' expr 'then' stat ('else' stat)?
    |   'return' expr? ';' 
    |   expr '=' expr ';' // assignment
    |   expr ';'          // func call
    ;

expr:   ID '(' exprList? ')'    // func call like f(), f(x), f(1,2)
    |   expr '[' expr ']'       // array index like a[i], a[i][j]
    |   '-' expr                // unary minus
    |   '!' expr                // boolean not
    |   expr '*' expr
    |   expr ('+'|'-') expr
    |   expr '==' expr          // equality comparison (lowest priority op)
    |   ID                      // variable reference
    |   INT
    |   '(' expr ')'
    ;

exprList : expr (',' expr)* ;   // arg list

ID  :   LETTER (LETTER | [0-9])* ;
fragment
LETTER : [a-zA-Z] ;

INT :   [0-9]+ ;

WS  :   [ \t\n\r]+ -> channel(1) ;  // channel(1)

SL_COMMENT
    :   '//' .*? '\n' -> channel(2)   // channel(2)
    ;
