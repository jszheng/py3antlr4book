grammar CppStat;

stat:   decl ';'  {print("decl "+$decl.text)}
    |   expr ';'  {print("expr "+$expr.text)}
    ;

decl:   ID ID           // E.g., "Point p"
    |   ID '(' ID ')'   // E.g., "Point (p)", same as ID ID
    ;
    
expr:   INT             // integer literal
    |   ID              // identifier
    |   ID '(' expr ')' // function call
    ;

ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;
WS  :   [ \t\n\r]+ -> skip ;
