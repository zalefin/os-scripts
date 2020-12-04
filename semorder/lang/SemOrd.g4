grammar SemOrd;

init: process NEWLINE sem NEWLINE terminal (NEWLINE constraint?)*;

process: 'process' ID (COMMA ID)*;
sem: 'sem' defin (COMMA defin)* ;
defin: ID EQUALS INT ;
terminal: 'terminal' INT ;
constraint: 'constraint' expr ;


expr: expr cmp expr
    | expr boolop expr
    | ID
    | '(' expr ')'
    ;

cmp: (GT|LT) ;
boolop: (LAND|LOR|LNOT) ;

GT: '>' ;
LT: '<' ;

LAND: '&' ;
LOR: '|' ;
LNOT: '!' ;

INT: [0-9]+ ;
ID: ([a-zA-Z_0-9])+ ;
COMMA: ',';
SEMICOLON: ';';
EQUALS: '=';
NEWLINE: '\r'? '\n' ;
WS: ' '+ -> skip ;
