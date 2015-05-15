grammar CSV;

@header {
from pprint import pprint

}

/** Derived from rule "start : hdr row+ ;" */
start
locals [i=0]
     : hdr ( rows+=row[$hdr.text.split(',')] {$i+=1} )+
       {
print(str($i)+" rows");
for r in $rows:
    print("row token interval: "+str(r.getSourceInterval()))
       }
     ;

hdr : row[None] {print("header: '"+$text.strip()+"'")} ;

row[columns] returns [values]
locals [col=0]
@init {
$values = {}
}
@after {
if ($values != None) or (len($values) > 0):
    pprint($values)
}
    :   field
        {
if ($columns!=None) :
    $values[$columns[$col].strip()] = $field.text.strip()
    $col += 1
        }
        (   ',' field
            {
if ($columns!=None) :
    $values[$columns[$col].strip()] = $field.text.strip()
    $col += 1
            }
        )* '\r'? '\n'
    ;

field
    :   TEXT
    |   STRING
    |
    ;

TEXT : ~[,\n\r"]+ ;
STRING : '"' ('""'|~'"')* '"' ; // quote-quote is an escaped quote
