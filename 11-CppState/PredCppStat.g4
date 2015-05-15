grammar PredCppStat;

@parser::header {
}

@parser::members {
@property
def types_table(self):
    try:
        return self._types_table
    except AttributeError:
        self._types_table = ['T']
        return self._types_table

def istype(self):
    if self.getCurrentToken().text in self.types_table:
        return True
    else:
        return False
}

stat:   decl ';'  {print("decl "+$decl.text);}
    |   expr ';'  {print("expr "+$expr.text);}
    ;

decl:   ID ID                         // E.g., "Point p"
    |   {self.istype()}? ID '(' ID ')'     // E.g., "Point (p)", same as ID ID
    ;

expr:   INT                           // integer literal
    |   ID                            // identifier
    |   {not self.istype()}? ID '(' expr ')'  // function call
    ;

ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;
WS  :   [ \t\n\r]+ -> skip ;
