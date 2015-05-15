/** Simple statically-typed programming language with functions and variables
 *  taken from "Language Implementation Patterns" book.
 */
grammar Cymbol;

top:   (functionDecl | varDecl)+ ;

varDecl
    :   primtype ID ('=' expr)? ';'
    ;
primtype:   'float' | 'int' | 'void' ; // user-defined types

functionDecl
    :   primtype ID '(' formalParameters? ')' block // "void f(int x) {...}"
    ;

formalParameters
    :   formalParameter (',' formalParameter)*
    ;
formalParameter
    :   primtype ID
    ;

block:  '{' stat* '}' ;   // possibly empty statement block

stat:   block
    |   varDecl
    |   'if' expr 'then' stat ('else' stat)?
    |   'return' expr? ';' 
    |   expr '=' expr ';' // assignment
    |   expr ';'          // func call
    ;

expr:   ID '(' exprList? ')'    # Call
    |   expr '[' expr ']'       # Index
    |   '-' expr                # Negate
    |   '!' expr                # Not
    |   expr '*' expr           # Mult
    |   expr ('+'|'-') expr     # AddSub
    |   expr '==' expr          # Equal
    |   ID                      # Var
    |   INT                     # Int
    |   '(' expr ')'            # Parens
    ;

exprList : expr (',' expr)* ;   // arg list

K_FLOAT : 'float';
K_INT   : 'int';
K_VOID  : 'void';
ID  :   LETTER (LETTER | [0-9])* ;

fragment
LETTER : [a-zA-Z] ;

INT :   [0-9]+ ;

WS  :   [ \t\n\r]+ -> skip ;

SL_COMMENT
    :   '//' .*? '\n' -> skip
    ;
