lexer grammar XMLLexer;

// Default "mode": Everything OUTSIDE of a tag
OPEN        :   '<'                 -> pushMode(INSIDE) ;
COMMENT     :   '<!--' .*? '-->'    -> skip ;
EntityRef   :   '&' [a-z]+ ';' ;
TEXT        :   ~('<'|'&')+ ;           // match any 16 bit char minus < and &

// ----------------- Everything INSIDE of a tag ---------------------
mode INSIDE;

CLOSE       :   '>'                 -> popMode ; // back to default mode
SLASH_CLOSE :   '/>'                -> popMode ;
EQUALS      :   '=' ;
STRING      :   '"' .*? '"' ;
SlashName   :   '/' Name ;
Name        :   ALPHA (ALPHA|DIGIT)* ;
S           :   [ \t\r\n]           -> skip ;

fragment
ALPHA       :   [a-zA-Z] ;

fragment
DIGIT       :   [0-9] ;
