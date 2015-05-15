grammar Data;

top : group+ ;

group: INT sequence[$INT.int] ;

sequence[n]
locals [i=0]
     : ( {$i<$n}? INT {$i=$i+1;} )* // match n integers
     ;
     
INT :   [0-9]+ ;             // match integers
WS  :   [ \t\n\r]+ -> skip ; // toss out all whitespace
