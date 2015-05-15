grammar LExpr;

s : e ;

e : e MULT e 		# Mult
  | e ADD e 		# Add
  | INT        		# Int
  ;

MULT: '*' ;
ADD : '+' ;
INT : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
