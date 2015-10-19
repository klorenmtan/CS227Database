from Query import *
from FileReader import *
from Select import *
from Metadata import *
from Data import *
from LexerParser import *

class Main:
	database={}
	md=Metadata()
		
	statement=''
	while statement!='quit':
		statement=input("SQL>")
		
		if statement == 'quit;':
			break
		elif statement == 'desc payment;':
			md.showMetaData('payment')
			
		elif statement == 'desc delivery;':
			md.showMetaData('delivery')
		elif statement == 'desc si;':
			md.showMetaData('si')
		elif statement == 'desc customer;':
			md.showMetaData('customer')
		elif statement == 'desc product;':
			md.showMetaData('product')
		
		else:
			lexer = SqlLexer().build()
			parser = SqlParser().build()
			
			result = parser.parse(statement)
			statement=result
			print(result)
			if result == None:
				print("Input Error")
			else:
				if ';' in statement:
					statement=statement[:-2]
				else:
					printf("Error expecting ;")			
				q1=Query(statement,database)
				q1.classify_query();
			
		


	

	

