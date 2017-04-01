grammar MokadiGrammar;

parse
    : mokadi expression_stmt  EOF
    ;
    
/////////////
// expression
/////////////

expression_stmt
    : expression
    | ('(' expression ')')
    ;

expression
    : slides_stmt
    | anything_stmt
    ;
    
slides_stmt
    : verb presentation (integer_number slides integer_number)?
    ;
    
anything_stmt
    : word_name word_name* question?
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
    
presentation
    : Presentation
    | 'powerpoint'
    ;
    
Presentation
    : 'pr' E_CODE 'sentation'
    ;    
    
slides
    : 'slides'
    | 'slide'
    | 'transparent'
    ;
    
verb
    : 'lit'
    | 'voir'
    | 'list'
    | 'lire'
    | 'liste'
    | 'lister'
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
    
question
    : '?'
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
    
fragment E_CODE
    : '\u00E9' | 'é' | 'e'
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

