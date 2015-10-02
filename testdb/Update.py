#UPDATE Class
#Venus Retuya
#Wens Navallo
#

from Update import * 
from FileReader import *
from Metadata import *
class Update:

	def __init__(self,statements,database):	
		self.statementList = statements;
		self.data =[];
		global meta
		meta = Metadata();
		self.qlength = len(statements);
		self.database = database;
		

	
	def DissectUpdate(self):
		self.TblName = [];
		self.PrimaryKey = [];
		self.SetColNameToUpdate = [];
		self.SetColValToUpdate =[];
		self.WhereColName = [];
		self.WhereColVal = [];
		self.WhereComOperator = [];
		self.WhereLogicOperator = [];
		
		
		lUpdateStatement = self.statementList
		print('Update Statement:' + str(lUpdateStatement))
		
		#get Table Name
		self.TblName.append(self.statementList[1])
		print('Table Name:' + str(self.TblName))
		
		#Dissect SET and WHERE CLAUSE 
		
		if 'where' in lUpdateStatement:
			
			#SET CLAUSE
			iSetIndex = lUpdateStatement.index('set') # get the index of 'set'
			iWhereIndex = lUpdateStatement.index('where')  # get the index of 'where'
		
			lSetClause = lUpdateStatement[iSetIndex+1:iWhereIndex] # extract the set clause
			
		
			#Iterate to SetClause and assign the Column name and its value to self 
			for index in range(len(lSetClause)):				
				if lSetClause[index] == '=':
					self.SetColNameToUpdate.append(lSetClause[index - 1])
					self.SetColValToUpdate.append(lSetClause[index + 1])	
				
			print('Set Column Name:' + str(self.SetColNameToUpdate))
			print('Set Column Value:' + str(self.SetColValToUpdate))		 
		
			#WHERE CLAUSE
			lWhereClause = lUpdateStatement[iWhereIndex+1:len(lUpdateStatement)] # extract the where clause
			
			#Comparison Operators
			lCompareOperator =['=','>','<','=>','=<','<>'];
			
			#LogicalOperator
			lLogicalOperator = ['and','or','not'];
			
			#Iterate to Where Clause and assign the Column names and its value, comparison and logical operators to self 	
			for index in range(len(lWhereClause)):			
				if lWhereClause[index] in lCompareOperator:
					self.WhereComOperator.append(lWhereClause[index])
					self.WhereColName.append(lWhereClause[index-1]) 
					self.WhereColVal.append(lWhereClause[index+1])
				else:
					if lWhereClause[index] in lLogicalOperator:
						self.WhereLogicOperator.append(lWhereClause[index])
				
			print('Where Column Name :' + str(self.WhereColName))
			print('Where Comparison Operator:' + str(self.WhereComOperator))
			print('Where Column Value:' + str(self.WhereColVal))
			print('Where Logical Operator:' + str(self.WhereLogicOperator))
			
		else:
			#Update statement without Where Clause
			iSetIndex = lUpdateStatement.index('set')
			lSetClause = lUpdateStatement[iSetIndex+1:len(lUpdateStatement)]
		
			#Iterate to SetClause and assign the Column name and Value to self
			for index in range(len(lSetClause)):				
				if lSetClause[index] == '=':
					self.SetColNameToUpdate.append(lSetClause[index - 1])
					self.SetColValToUpdate.append(lSetClause[index + 1])
								
			print('Set Column Name:' + str(self.SetColNameToUpdate))
			print('Set Column Value:' + str(self.SetColValToUpdate))
			
		

	def CheckUpdate(self):
		
		print('Result of CheckUpdate')
		
		#check if the table is existing		
		if not(meta.checkTableExist(self.TblName)):
			sTableName = self.TblName[0]
			print("Table '" + sTableName +"' does not exist! ")
			return False
			
		else:
			#check if the set columns are existing
			for ColumnName in self.SetColNameToUpdate:						
				if not(meta.checkcolumnExist(self.TblName[0], ColumnName)):
					print("Unknown column name '" + str(ColumnName) + "' in set field list!")
					return False					
					
			#check if the where columns are existing
			for ColumnName in self.WhereColName:
				if not(meta.checkcolumnExist(self.TblName[0], ColumnName)):
					print("Unknown Column name '" + str(ColumnName) + "' in where field list!")
					return False
		

			print('Table name and column names have been checked!') 
			
							

	
	def SetColumnValue(Clause):
		SetColVal = {}
		for index in range(len(Clause)):			
			if Clause[index] == '=':
				SetColVal[Clause[index-1]] = Clause[index+1]
		print('Where Column Name and Value:' + str(SetColVal))
		return SetColVal		

			
		
	def MakeUpdate(self): 
		#val=self.UpdateTree()
		#if val==True:		
		#	self.performUpdate()		
		self.DissectUpdate();
		self.CheckUpdate();
		self.PerformUpdate();
			
			
	def PerformUpdate(self):
		self.fetch_data()
		self.GetPK()
		#perform operations pass the list of operations
		#returns list of primary key + data
		#prints it
			
	def GetPK(self):
		
		print('Result of Get Primary Key')
		print(self.database.keys())
		print(str(Data.PrintDataALL(self.TblName,self.database)))
		
		
	
	def fetch_data(self):
		array1 = {}
		
		for i in range(0,len(self.TblName)):
			if not(self.TblName[i] in self.database.keys()):
				filer=FileReader(self.TblName[i])
				filer.fileRead()
				array1=filer.hashData()
				self.database[self.TblName[i]]=array1				

		print('Result of fetch_data')
		print(self.database.keys())
		#print (str(self.database[self.TblName[i]]))
	
	

	
