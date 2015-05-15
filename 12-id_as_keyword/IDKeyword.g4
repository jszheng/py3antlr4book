grammar IDKeyword;

prog: stat+ ;

stat: 'if' expr 'then' stat
    | 'call' id_rule ';'
    | ';'
    ;

expr: id_rule ;

id_rule  :   'if' | 'call' | 'then' | ID ;

ID : [a-z]+ ;
WS : [ \r\n]+ -> skip ;
