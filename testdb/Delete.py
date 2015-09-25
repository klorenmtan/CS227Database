from Delete import * 
from FileReader import *
from Metadata import *
import itertools

	
class Delete:


	def __init__(self,statements,database):
	
		self.statementList = statements;
		self.data =[];
		global meta
		meta = Metadata();
		self.qlength = len(statements);
		self.database = database;

	def split_by_logic(self,iterable,splitters): 
		return [list(g) for k,g in itertools.groupby(iterable,lambda x:x in splitters) if not k]

	
	def select_tree(self):
		self.targetPrint=[];
		self.tblname=[];
		self.where_operation=[]

		#get table name and target print
		for i in range(1,len(self.statementList)):
			if self.statementList[i] == "from":
				j=i+1	
				while(j<len(self.statementList)):
					if self.statementList[j]=="where":
						k=j+1
						break
					else:
						self.tblname.append(self.statementList[j])
					j=j+1
					k=len(self.statementList)			
				break				
				
			else:
				self.targetPrint.append(self.statementList[i])
		
		#check if the columns exist for target print
		self.targetPrint=list(filter(None,self.targetPrint))
		self.tblname=list(filter(None,self.tblname))		
		print(self.targetPrint)
		print(self.tblname)	
		#print(self.where_operation)
		status=0			
		print('vvvvv')
		print(self.targetPrint)
		print('aaaaaa')


		print('sada')
		#check if the table is existing
		for m in range(0,len(self.tblname)):
			if not(meta.checkTableExist(self.tblname[m])):
				print("Table Does Not Exist")
				return False				
			else:
				for j in range(k,len(self.statementList)):
					
					self.where_operation.append(self.statementList[j])

				
		#split muna bago check ng columns			
		#for the where clause
		if len(self.where_operation)> 0:
			for i in range(0,len(self.tblname)):
				for j in range(0,len(self.where_operation)):
					print(j)
					if not((self.where_operation[j]!= '<' or self.where_operation[j]!= '>' or self.where_operation[j]!= '=' or (self.where_operation[j].isDigit())) and self.where_operation[i] in meta.getAllColumns(self.tblname[i])):
						print(self.where_operation[j] + " Column Does Not Exist" )
						return False
		return True


	def make_delete(self): 
		print('make_delete')
		val=self.select_tree()
		print(val)
		if val==True:		
			self.perform_delete()
		
			

	def perform_delete(self):
		self.fetch_data()
		
		
		# if where is blank

		print(self.where_operation)
	
		#foreach row in self.database[self.tblname[0]]['2'] palitan yung [0]['2'] ng pang increment ng rows
		#print(self.database[self.tblname[0]]['2'][self.where_operation[0]]) 

		# if (self.database[self.tblname[0]]['2'][self.where_operation[0]]) 
		
		self.perform_operations()
		#perform operations pass the list of operations
		#returns list of primary key + data
		#prints it

	def perform_operations(self):
		
		#no where clause
		# print all keys in table when there is no where statement found

		if (len(self.where_operation) == 0):
			print("delete all")
			for i in range(0,len(self.tblname)):
				print(self.database[self.tblname[i]].keys())
				print(type(self.database[self.tblname[i]]))
			print('end delete all')

		if (len(self.where_operation) == 3):
			print('delete with single where clause')
			print(self.evaluate_expression(self.where_operation[0],self.where_operation[1],self.where_operation[2]))
			print('end delete single')

		
		if (len(self.where_operation) > 3):
		
			#gumawa ng dalawang list una yung mga io-or then yung mga ie-and


			print('multiple where')

			andKeyTable=[]
			orKeyTable=[]
			result=[]

			andSplitted = self.split_by_logic(self.where_operation, ('and'))

			for i in range(0,len(andSplitted)):


				if (len(andSplitted[i])==3):
					print(andSplitted[i])
					#add primary key to list
					print(self.evaluate_expression(andSplitted[i][0],andSplitted[i][1],andSplitted[i][2]))
					andKeyTable.append(self.evaluate_expression(andSplitted[i][0],andSplitted[i][1],andSplitted[i][2]))


				else:
					print('split by or then evaluate_expression')

					print('+++++++++++++++++++++++++++')
					orSplitted = self.split_by_logic(andSplitted[i], 'or')
					for j in range(0,len(orSplitted)):
						print('===============orSplitted '+ str(j) + ' value :' )
						print(orSplitted[j])

						if (len(orSplitted[j])==3):
							#add primary key to list
							print(self.evaluate_expression(orSplitted[j][0],orSplitted[j][1],orSplitted[j][2]))
							orKeyTable.append(self.evaluate_expression(orSplitted[j][0],orSplitted[j][1],orSplitted[j][2]))
					
					orResult=[]			
					for j in range(0,len(orKeyTable)-1):
						orResult= list(set(orKeyTable[j]) | set(orKeyTable[j+1]) )
					andKeyTable.append(orResult)
					
									
					print('-----------------------------')

				for i in range(0,len(andKeyTable)-1):
					result= list(set(andKeyTable[i]) & set(andKeyTable[i+1]) )				

				print('and result')
				print(result)
				print('and result')
			#split where operation
				print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
				print('end multiple where')



		#for i in range (0,len(self.where_operation)):
		#	print("ops ",self.where_operation[i],"--->type ",type(self.where_operation[i]))
			
		
	def fetch_data(self):
		array1 = {}
		for i in range(0,len(self.tblname)):
			if not(self.tblname[i] in self.database.keys()):
				filer=FileReader(self.tblname[i])
				filer.fileRead()
				array1=filer.hashData()	
				self.database[self.tblname[i]]=array1

				

	#def buildTree(self):
		
	'''	
	def check_show(self):
		for i in range(1,(len(self.statementList))):			
			if(self.statementList[i]=="*"):
				if (self.meta).checkTableExist(self.statementList[i+1]):
											
					if self.statementList[i+1] in self.database:
						filer.printData(self.statementList[i+1])	
					else:						
						filer.fileRead(self.data)
						self.database=filer.hashData();
						filer.printData(self.statementList[i+1])				
						break
				
				else:
					print ("Table Does Not Exist")
					break
			#else:
				#check columns
	
	'''	
	
		
  
		
	def evaluate_expression(self,operand1,operation,operand2):
	

		# operand1 = self.where_operation[0]
		# operand2 = self.where_operation[2]
		# operation = self.where_operation[1] 

		matches=[]

			if (operand1 in meta.getAllColumns(self.tblname[i])):
				columnName = operand1
				value = operand2
			else:
				columnName = operand2
				value = operand1

				
			for key in self.database[self.tblname[i]].items():
				if (operation == '='):
					if (str(key[1][columnName]) == value):
						print('key=================')
						print(key[0])
						print('key=================')
						matches.append(key[0])
					
				if(operation == '!='):
					if (str(key[1][columnName]) != value):
						matches.append(key[0])
	
				if (operation == '>'):
					if ((key[1][columnName]) > float(value)):
						matches.append(key[0])
	
				if (operation == '<'):
					if ((key[1][columnName]) < float(value)):
						matches.append(key[0])
		return matches

