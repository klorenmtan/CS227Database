from Select import * 
from FileReader import *
from Metadata import *
class Select:

	def __init__(self,statements,database):
	
		self.statementList = statements;
		self.data =[];
		global meta
		meta = Metadata();
		self.qlength = len(statements);
		self.database = database;

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
				
		for m in range(0,len(self.targetPrint)):
			if self.targetPrint[m] =="*":
				break
			else:
				for n in range(0,len(self.tblname)):
					if not(meta.checkcolumnExist(self.tblname[n],self.targetPrint[m])):
						print ("Column Does Not Exist")
						return False
		
		#check if the table is existing
		for m in range(0,len(self.tblname)):
			if not(meta.checkTableExist(self.tblname[m])):
				print("Table Does Not Exist")
				return False				
			else:
				for j in range(k,len(self.statementList)):
					
					self.where_operation.append(self.statementList[j])

				
		print(self.targetPrint)
		print(self.tblname)	
		print(self.where_operation)				
		#for the where clause
		
		#print(self.where_operation)
		if len(self.where_operation)> 0:
			for i in range(0,len(self.tblname)):
				for j in range(0,len(self.where_operation)):
					if not((self.where_operation[j]!= '<' or self.where_operation[j]!= '>' or self.where_operation[j]!= '=' or (self.where_operation[j].isdigit())) and self.where_operation[i] in meta.getAllColumns(self.tblname[i])):
						print("Column Does Not Exist")
						return False
		return True
	def make_select(self): 
		val=self.select_tree()
		if val==True:
			self.where_operation=list(filter(None,self.where_operation))				
			print(self.where_operation)		
			self.perform_select()
		
			

	def perform_select(self):
		self.fetch_data()
		self.perform_operations()
		#perform operations pass the list of operations
		#returns list of primary key + data
		#prints it

	def perform_operations(self):
		result=[]
		self.counter=0
		statement=''

		for i in range (0,len(self.where_operation)):
			if self.where_operation[i] == '>':
				print("ops >")
			elif self.where_operation[i] == '<':
				print("ops <")
			elif self.where_operation[i] == '=':
				print("ops =")
			elif self.where_operation[i] == 'and':
				print("and")
			elif self.where_operation[i] == 'or':
				print("or")
			elif self.where_operation[i].isdigit():
				self.where_operation[i]=int(self.where_operation[i])
				print("int/digit: ",self.where_operation[i],"--->type ",type(self.where_operation[i]))
				
			else:
				print("data: ",self.where_operation[i],"--->type ",type(self.where_operation[i]))
			
			
	def fetch_data(self):
		array1 = {}
		
		for i in range(0,len(self.tblname)):
			if not(self.tblname[i] in self.database.keys()):
				filer=FileReader(self.tblname[i])
				filer.fileRead()
				array1=filer.hashData()
				self.database[self.tblname[i]]=array1
				

		print(self.database.keys())

				

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
	
		
  
		
