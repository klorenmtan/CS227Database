from Select import * 
from FileReader import *
from Metadata import *
from Semantic import *
import time
import datetime

class Update:
	def __init__(self,statements,database,targetColumn,tblname,newValues,whereOperation):
		#Update(stat,self.database,targetPrint,tblnames,join_clause,where_operation);
		self.statementList = statements;
		self.data =[];
		global meta
		meta = Metadata();
		self.qlength = len(statements);
		self.database = database;
		self.targetColumn=targetColumn
		self.tblname=tblname
		self.newValues=newValues
		self.where_operation=whereOperation

	def perform_update(self):
		self.fetch_data()
		self.perform_operations()

	def perform_operations(self):
		if len(self.where_operation) == 0:
			keys=list(self.database[self.tblname[0]].keys())
						
			for i in range(0,len(self.database[self.tblname[0]])):
				for j in range(0,len(self.targetColumn)):
					self.database[self.tblname[0]][keys[i]][self.targetColumn[j]]=self.newValues[j] 
			
			#print(self.database)
			if len(keys) == 1:
				print(len(keys),"row affected")
			else:
				print(len(keys),"rows affected")

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

			#print(pk)
			
			for i in range(0,len(pk)):
				for j in range(0,len(self.targetColumn)):
					self.database[self.tblname[0]][str(pk[i])][self.targetColumn[j]]=self.newValues[j] 
				
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
