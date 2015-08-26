
# -----------------------------------------------------------------------------
# update_select_delete.py
#
# -----------------------------------------------------------------------------

tokens = [
    'ID','ALL','DOT','COMMA','LPAREN','RPAREN','EQ','NEQ','GT','LT','EOL','STRING','INT','DOUBLE'
]

reserved = {
    'update'    :   'UPDATE',
    'set'       :   'SET',
    'select'    :   'SELECT',
    'delete'    :   'DELETE',
    'from'      :   'FROM',
    'join'      :   'JOIN',
    'natural'   :   'NATURAL',
    'on'        :   'ON',
    'where'     :   'WHERE',
    'and'       :   'AND',
    'or'        :   'OR'
}

tokens += reserved.values()

def t_INT(t):
    # for what Python accepts, then use eval
    r'\d+'
    t.value = int(t.value)    
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    # redis is case sensitive in hash keys but we want the sql to be case insensitive,
    # so we lowercase identifiers 
    t.value = t.value.lower()
    return t

def t_STRING(t):
    # TODO: unicode...
    # Note: this regex is from pyparsing, 
    # TODO: may be better to refer to http://docs.python.org/reference/lexical_analysis.html 
    '(?:"(?:[^"\\n\\r\\\\]|(?:"")|(?:\\\\x[0-9a-fA-F]+)|(?:\\\\.))*")|(?:\'(?:[^\'\\n\\r\\\\]|(?:\'\')|(?:\\\\x[0-9a-fA-F]+)|(?:\\\\.))*\')'
    t.value = eval(t.value) 
    #t.value[1:-1]
    return t

# Tokens
t_ALL       =   r'\*'
t_COMMA     =   r'\,'
t_DOT       =   r'\.'
t_LPAREN    =   r'\('
t_RPAREN    =   r'\)'
t_GT        =   r'>'
t_LT        =   r'<'
t_EOL       =   r';'
t_EQ        =   r'='
t_NEQ       =   r'!='
t_DOUBLE    =   r'\d+\.\d*'

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

#data = input()
#lexer.input(data)
#while True:
#    tok = lexer.token()
#    if not tok:
#        break
#    print(tok)


# Parsing Rules

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NEQ', 'LT', 'GT')
)
            
def p_statement(p):
    ''' statement : update_statement
                  | select_statement
                  | delete_statement '''
    
    p[0] = p[1]

def p_update_statement(p):
    ''' update_statement : UPDATE ID SET set_clause_list EOL
                         | UPDATE ID SET set_clause_list WHERE search_condition EOL '''

def p_select_statement(p):
    ''' select_statement : SELECT select_columns FROM id_list EOL
                         | SELECT select_columns FROM id_list WHERE search_condition EOL
                         | SELECT select_columns FROM id_list join_clause 
                         | SELECT select_columns FROM id_list join_clause WHERE search_condition EOL '''

def p_delete_statement(p):
    ''' delete_statement : DELETE FROM ID EOL
                         | DELETE FROM ID WHERE search_condition EOL '''

def p_select_columns(p):
    ''' select_columns : ALL
                       | id_list '''

def p_set_clause_list(p):
    ''' set_clause_list : id_list EQ literal
                        | id_list EQ literal COMMA set_clause_list '''

def p_join_clause(p):
    ''' join_clause : JOIN ID ON ID EQ ID EOL
                    | JOIN ID ON ID DOT ID EQ ID DOT ID EOL
                    | NATURAL JOIN ID EOL
                    | JOIN ID ON ID EQ ID join_clause EOL
                    | JOIN ID ON ID EQ ID search_condition EOL  
                    | JOIN ID ON ID DOT ID EQ ID DOT ID search_condition EOL
                    | JOIN ID ON ID DOT ID EQ ID DOT ID join_clause EOL
                    | NATURAL JOIN ID join_clause EOL '''
    
def p_search_condition(p):
    ''' search_condition : search_condition OR search_condition
                         | search_condition AND search_condition
                         | AND search_condition
                         | OR search_condition
                         | LPAREN search_condition RPAREN
                         | comparison_predicate '''

def p_comparison_predicate(p):
    ' comparison_predicate : value comp_op value '

def p_comp_op(p):
    ''' comp_op : EQ
                | NEQ
                | GT
                | LT '''
    
def p_id_list(p):
    ''' id_list : ID
                | id_list COMMA ID '''
    
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_value(p):
    ''' value : ID
              | literal '''

def p_literal(p):
    ''' literal : INT
                | DOUBLE
                | STRING '''
    p[0] = p[1]


import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('sql > ')   # Use raw_input on Python 2
        s=s.lower()
    except EOFError:
        break
    if s == 'quit':
       break
    parser.parse(s)
