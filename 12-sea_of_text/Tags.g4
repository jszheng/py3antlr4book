grammar Tags;
entry : (TAG|ENTITY|TEXT|CDATA)* ;

COMMENT : '<!--' .*? '-->' -> skip ;
CDATA : '<![CDATA[' .*? ']]>' ;
TAG : '<' .*? '>' ; // must come after other tag-like structures
ENTITY : '&' .*? ';' ;
TEXT : ~[<&]+ ;     // any sequence of chars except < and & chars
