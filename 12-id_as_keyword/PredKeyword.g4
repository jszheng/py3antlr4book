grammar PredKeyword;

prog: stat+ ;

stat: keyIF expr 'then' stat
    | keyCALL ID ';'
    | ';'
    ;

expr: ID
    ;

keyIF :   {self._input.LT(1).text == "if"}? ID ;

keyCALL : {self._input.LT(1).text == "call"}? ID ;

ID : 'a'..'z'+ ;
WS : (' '|'\n')+ -> skip;
