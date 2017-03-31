grammar MokadiGrammar;

parse
    : mokadi expression_stmt  EOF
    ;
    
/////////////
// mokadi
////////////

mokadi
    : 'MOKADI'
    | 'mokadie'
    | 'leocadie'
    | 'Leocadie'
    ;
    
/////////////
// expression
/////////////

expression_stmt
    : expression
    | ('(' expression ')')
    ;

expression
    : word_name word_name*
    ;

////////
// rules
////////

word_name
    : Identifier
    | constant
    | operator
    ;
    
operator
    : '+' | '-' | '*' | '/' | '%' | '&&' | '||' | '==' | '!=' | '<=' | '>=' | '>' | '<'
    ;

constant
    : integer_number
    | real_number
    | string_literal
    ;

string_literal
    : STRING
    ;

integer_number
    : Sign? Digits
    ;
    
real_number
    : (Sign? Digits '.' Digits ('e' Sign? Digits)?)
    | (Sign? Digits 'e' Sign? Digits)
    ;
    

/////////
// tokens
/////////

Digits
    : DIGIT+
    ;

Identifier
    : LETTER LETTER_DIGIT*
    ;
    
STRING
    : STRING_DOUBLE_QUOTE
    | STRING_QUOTE
    ;
    
STRING_DOUBLE_QUOTE
    : '"' (NO_DOUBLE_QUOTE | '\\"')* '"'
    ;
    
STRING_QUOTE
    : '\'' (NO_QUOTE | '\\\'')* '\''
    ;
    
fragment NO_QUOTE
    : ~[']
    ;

fragment NO_DOUBLE_QUOTE
    : ~["]
    ;

fragment LETTER_DIGIT
    : LETTER | DIGIT
    ;
    
fragment DIGIT
    : [0-9]
    ;

fragment LETTER      
    : [a-zA-Z\u0080-\u00FF_] 
    ;
    
LINE_COMMENT:   '#' .*? '\r'? '\n' {skip();} ;

WS          :   [ \t\r\n] -> skip ;

