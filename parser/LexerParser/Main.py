from FileReader import *
from LexerParser import *
from Metadata import *
from Data import *
class Main:
        database={}
        md=Metadata()

        statement=''
        while statement!='quit':
                statement=input("SQL>")
                statement=statement.lower()
                statement=statement.replace(","," ")
                if statement == 'quit':
                        break
                else:
                        lexer = SqlLexer().build()
                        parser = SqlParser().build()
                        result = parser.parse(statement)
                        print ('parse result >>> {}' .format(result))
                        #q1=Query(statement,database)
			#q1.classify_query()
		
		


	

	

