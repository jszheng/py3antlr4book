grammar Keywords;
// @lexer::header {
// }

// explicitly define keyword token types to avoid implicit def warnings
tokens { BEGIN, END, IF, THEN, WHILE }

// @lexer::members {
// }

stat:   BEGIN stat* END 
    |   IF expr THEN stat
    |   WHILE expr stat
    |   ID '=' expr ';'
	;

expr:   INT | CHAR ;

ID  :   [a-zA-Z]+
        {
if self.text in self.keywords:
    self.type = self.keywords.get(self.text)
        }
    ;

/** Convert 3-char 'x' input sequence to string x */
CHAR:   '\'' . '\'' {self.text = self.text[1]} ;

INT :   [0-9]+ ;

WS  :   [ \t\n\r]+ -> skip ;
