/** Grammar from tour chapter augmented with actions */
grammar Expr;

@header {
}

@parser::members {
@property
def memory(self):
    if not hasattr(self, '_map'):
        setattr(self, '_map', {})
    return self._map
    
@memory.setter
def memory_setter(self, value):
    if not hasattr(self, '_map'):
        setattr(self, '_map', {})
    self._map = value
    
def eval(self, left, op, right):
    if   ExprParser.MUL == op.type:
        return left * right
    elif ExprParser.DIV == op.type:
        return left / right
    elif ExprParser.ADD == op.type:
        return left + right
    elif ExprParser.SUB == op.type:
        return left - right
    else:
        return 0
}

stat:   e NEWLINE           {print($e.v);}
    |   ID '=' e NEWLINE    {self.memory[$ID.text] = $e.v}
    |   NEWLINE                   
    ;

e returns [int v]
    : a=e op=('*'|'/') b=e  {$v = self.eval($a.v, $op, $b.v)}
    | a=e op=('+'|'-') b=e  {$v = self.eval($a.v, $op, $b.v)}
    | INT                   {$v = $INT.int}    
    | ID
      {
id = $ID.text
$v = self.memory.get(id, 0)
      }
    | '(' e ')'             {$v = $e.v}       
    ; 

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;

ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
