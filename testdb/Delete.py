from Select import * 
from FileReader import *
from Metadata import *
from Semantic import *

class Delete:
	
	def __init__(self,statements,database,tblname,whereOperation):

		self.statementList = statements;
		self.data =[];
		global meta
		meta = Metadata();
		self.qlength = len(statements);
		self.database = database;
		self.tblname=tblname
		self.where_operation=whereOperation


	def perform_delete(self):
		self.fetch_data()
		self.perform_operations()

	def perform_operations(self):
		if len(self.where_operation) == 0:
			key1=(list(self.database[self.tblname[0]].keys()))	
			print(key1)

			for i in range(0,len(key1)):
				del self.database[self.tblname[0]][str(key1[i])]
	
			if len(key1) == 1:
				print(len(key1),"row affected")	
			else:
				print(len(key1),"rows affected")
				
			

		else:
			pk=[]
			columns=[]
			result=[]
			result=Data.PrintDataALL(self.tblname,self.database)
			for j in range(0,len(self.tblname)):
				columns.extend(meta.getAllColumns(self.tblname[j]))
			r1=Select.classify_where(self.tblname,self.where_operation,result,columns)
			
			for i in range(0,len(r1)):
				pk.append(r1[i][0])

			print(pk)
			for i in range(0,len(pk)):
				del self.database[self.tblname[0]][str(pk[i])]
			if len(pk)==1:
				print(len(pk),"row affected")
			else:
				print(len(pk),"rows affected")
		

		return self.database

		
	def fetch_data(self):
		array1 = {}
		
		for i in range(0,len(self.tblname)):
			if not(self.tblname[i] in self.database.keys()):
				filer=FileReader(self.tblname[i])
				filer.fileRead()
				array1=filer.hashData()
				self.database[self.tblname[i]]=array1
				
