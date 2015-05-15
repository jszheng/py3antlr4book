grammar PropertyFile;

@members {
def startFile(self):
    pass
def finishFile(self):
    pass
def defineProperty(self, name, value):
    pass
}

top : {self.startFile()} prop+ {self.finishFile()};
prop : ID '=' STRING '\n' {self.defineProperty($ID, $STRING)};
ID   : [a-z]+ ;
STRING : '"' .*? '"' ;
