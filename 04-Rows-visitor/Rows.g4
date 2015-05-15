grammar Rows;

@parser::members {
@property
def column(self):
    return self._col

@column.setter
def column(self, value):
    self._col = value

}

rows: (row NL)+ ;

row
locals [i = 0]
    : (   STUFF
{
$i = $i + 1
if $i == self.column:
    print($STUFF.text)
}
      )+
    ;

TAB  :  '\t' -> skip ;   // match but don't pass to the parser
NL   :  '\r'? '\n' ;     // match and pass to the parser
STUFF:  ~[\t\r\n]+ ;     // match any chars except tab, newline
