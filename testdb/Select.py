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
		
		self.targetPrint=list(filter(None,self.targetPrint))
		self.tblname=list(filter(None,self.tblname))		
		print(self.targetPrint)
		print(self.tblname)	
		status=0			
		for m in range(0,len(self.targetPrint)):
			if self.targetPrint[m] =="*":
				status=1
				break
			else:
				for n in range(0,len(self.tblname)):
					
					if (meta.checkcolumnExist(self.tblname[n],self.targetPrint[m])):
						print(self.tblname[n],self.targetPrint[m])
						status=1
						continue
					else:
						status=0
											
		if status==0:						#print ("Column Does Not Exist")
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

				
					
		#for the where clause
		
		#print(self.where_operation)
		if len(self.where_operation)> 0:
			for i in range(0,len(self.tblname)):
				for j in range(0,len(self.where_operation)):
					if not((self.where_operation[j]!= '<' or self.where_operation[j]!= '>' or self.where_operation[j]!= '=' or (self.where_operation[j].isDigit())) and self.where_operation[i] in meta.getAllColumns(self.tblname[i])):
						print("Column Does Not Exist")
						return False
		return True
	def make_select(self): 
		val=self.select_tree()
		if val==True:		
			self.perform_select()

	def perform_select(self):
		self.fetch_data()
		self.perform_operations()
		
	def perform_operations(self):
		result=[]
		self.counter=0
		statement=''
		print(self.targetPrint)
		if len(self.where_operation) == 0:
			print("No where operation")
			if self.targetPrint[0]=='*':
				Data.PrintDataALL(self.tblname,self.database)
			else:
				Data.PrintColumn(self.tblname,self.targetPrint,self.database)
		else:
			print(self.where_operation)
			
			
			
	def fetch_data(self):
		array1 = {}
		
		for i in range(0,len(self.tblname)):
			if not(self.tblname[i] in self.database.keys()):
				filer=FileReader(self.tblname[i])
				filer.fileRead()
				array1=filer.hashData()
				self.database[self.tblname[i]]=array1
				

		#print(self.database.keys())

				


		
  
		
