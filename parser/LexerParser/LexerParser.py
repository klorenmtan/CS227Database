
# -----------------------------------------------------------------------------
# update_select_delete.py
#
# -----------------------------------------------------------------------------

from ply import lex, yacc


class SqlLexer:
    
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

    def t_INT(self, t):
        # for what Python accepts, then use eval
        r'\d+'
        #t.value = int(t.value)    
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = SqlLexer.reserved.get(t.value,'ID')    # Check for reserved words
        # redis is case sensitive in hash keys but we want the sql to be case insensitive,
        # so we lowercase identifiers 
        t.value = t.value.lower()
        return t

    def t_STRING(self, t):
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

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")
        
    def t_error(self, t):
        print('Illegal character {}' .value(t))
        #print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        
    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

    #data = input()
    #lexer.input(data)
    #while True:
    #    tok = lexer.token()
    #    if not tok:
    #        break
    #    print(tok)


class SqlParser:

    tokens = SqlLexer.tokens

    # Parsing Rules

    precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NEQ', 'LT', 'GT')
    )
                
    def p_statement(self, p):
        ''' statement : update_statement
                      | select_statement
                      | delete_statement '''

        p[0] = p[1]

    def p_update_statement(self, p):
        ''' update_statement : UPDATE ID SET set_clause_list EOL
                             | UPDATE ID SET set_clause_list WHERE search_condition EOL '''

        if len(p) == 6:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5]
        else:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6] + " " + p[7]

    def p_select_statement(self, p):
        ''' select_statement : SELECT select_columns FROM id_list EOL
                             | SELECT select_columns FROM id_list join_clause EOL
                             | SELECT select_columns FROM id_list WHERE search_condition EOL
                             | SELECT select_columns FROM id_list join_clause WHERE search_condition EOL '''
        if len(p) == 6:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5]
        elif len(p) == 7:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6]
        elif len(p) == 8:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6] + " " + p[7]
        else:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6] + " " + p[7] + " " + p[8]

    def p_delete_statement(self, p):
        ''' delete_statement : DELETE FROM ID EOL
                             | DELETE FROM ID WHERE search_condition EOL '''

        if len(p) == 5:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4]
        else:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6]

    def p_select_columns(self, p):
        ''' select_columns : ALL
                           | id_list '''

        p[0] = p[1]

    def p_set_clause_list(self, p):
        ''' set_clause_list : ID EQ literal
                            | ID EQ literal COMMA set_clause_list '''

        if len(p) == 4:
            p[0] = p[1] + " " + p[2] + " " + p[3]
        else:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5]

    def p_join_clause(self, p):
        ''' join_clause : NATURAL JOIN ID
                        | NATURAL JOIN ID join_clause
                        | join_list ON ID EQ ID
                        | join_list ON ID EQ ID join_clause
                        | join_list ON ID EQ ID join_search_condition
                        | join_list ON ID DOT ID EQ ID DOT ID
                        | join_list ON ID DOT ID EQ ID DOT ID join_clause
                        | join_list ON ID DOT ID EQ ID DOT ID join_search_condition '''

        if len(p) == 4:
            p[0] = p[1] + " " + p[2] + " " + p[3]
        elif len(p) == 5:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4]
        elif len(p) == 6:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5]
        elif len(p) == 7:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6]
        elif len(p) == 10:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6] + " " + p[7] + " " + p[8] + " " + p[9]
        else:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6] + " " + p[7] + " " + p[8] + " " + p[9] + " " + p[10]

    def p_join_list(self, p):
        ''' join_list : JOIN ID
                      | JOIN ID join_list '''
        
        if len(p) == 3:
            p[0] = p[1] + " " + p[2]
        elif len(p) == 4:
            p[0] = p[1] + " " + p[2] + " " + p[3]
       
    def p_join_search_condition(self, p):
        ''' join_search_condition : AND join_search_condition
                                  | OR join_search_condition
                                  | LPAREN join_search_condition RPAREN
                                  | comparison_predicate '''

        if len(p) == 3:
            p[0] = p[1] + " " + p[2]
        elif len(p) == 4:
            p[0] = p[1] + " " + p[2] + " " + p[3]
        else:
            p[0] = p[1]

    def p_search_condition(self, p):
        ''' search_condition : search_condition OR search_condition
                             | search_condition AND search_condition
                             | LPAREN search_condition RPAREN
                             | comparison_predicate '''

        if len(p) == 4:
            p[0] = p[1] + " " + p[2] + " " + p[3]
        else:
            p[0] = p[1]
        
    def p_comparison_predicate(self, p):
        ' comparison_predicate : value comp_op value '

        p[0] = p[1] + " " + p[2] + " " + p[3]

    def p_comp_op(self, p):
        ''' comp_op : EQ
                    | NEQ
                    | GT
                    | LT '''

        p[0] = p[1]
        
    def p_id_list(self, p):
        ''' id_list : ID
                    | ID DOT ID
                    | id_list COMMA ID
                    | id_list COMMA ID DOT ID '''
        
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            if p[2] == '.':
                p[0] = p[1] + " " + p[2] + " " + p[3]
            else: 
                p[0] = p[1] + " " + p[3]
        else:
            p[0] = p[1] + " " + p[3] + " " + p[4] + " " + p[5]

    def p_inner_select_statement(self, p):
        ''' inner_select_statement : SELECT select_columns FROM id_list
                                   | SELECT select_columns FROM id_list join_clause
                                   | SELECT select_columns FROM id_list WHERE search_condition
                                   | SELECT select_columns FROM id_list join_clause WHERE search_condition '''

        if len(p) == 5:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4]
        elif len(p) == 6:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5]
        elif len(p) == 7:
            p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6]
        else:
            p[0] = p[1] +  " " + p[2] + " " + p[3] + " " + p[4] + " " + p[5] + " " + p[6] + " " + p[7]

    def p_value(self, p):
        ''' value : ID
                  | ID DOT ID 
                  | literal
                  | LPAREN inner_select_statement RPAREN '''

        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            p[0] = p[1] + " " + p[2] + " " + p[3]

    def p_literal(self, p):
        ''' literal : INT
                    | DOUBLE
                    | STRING '''
        p[0] = p[1]

    def p_error(self, p):
        print ("Syntax error in input") # TODO: at line %d, pos %d!" % (p.lineno)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser


#    while True:
#        try:
#            s = input('sql > ')   # Use raw_input on Python 2
#            s = s.lower()
#        except EOFError:
#            break
#        result = parser.parse(s)
#        print ('parse result >>> {}' .format(result))
