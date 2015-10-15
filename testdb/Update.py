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
					self.SetColValToUpdate.append(lSetClause[index + 1].replace("'",""))	
				
			print('Set Column Name:' + str(self.SetColNameToUpdate))
			print('Set Column Value:' + str(self.SetColValToUpdate))		 
		
			#WHERE CLAUSE
			lWhereClause = lUpdateStatement[iWhereIndex+1:len(lUpdateStatement)] # extract the where clause
			
			#Comparison Operators
			lCompareOperator =['=','!=','>','<'];
			
			#LogicalOperator
			lLogicalOperator = ['and','or'];
			
			#Iterate to Where Clause and assign the Column names and its value, comparison and logical operators to self 	
			for index in range(len(lWhereClause)):			
				if lWhereClause[index] in lCompareOperator:
					self.WhereComOperator.append(lWhereClause[index])
					self.WhereColName.append(lWhereClause[index-1]) 
					self.WhereColVal.append(lWhereClause[index+1].replace("'",""))
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
		
		#print('Result of CheckUpdate')
		
		#check if the table is existing		
		if not(meta.checkTableExist(self.TblName)):
			sTableName = self.TblName[0]
			print("Table '" + sTableName +"' does not exist! ")
			return False
			
		else:
			#check if the set columns are existing
			for ColumnName in self.SetColNameToUpdate:						
				if not(meta.checkcolumnExist(self.TblName[0], ColumnName)):
					print("Column name '" + str(ColumnName) + "' does not exist in '" + str(self.TblName[0]) + "' table!")
					return False					
					
			#check if the where columns are existing
			for ColumnName in self.WhereColName:
				if not(meta.checkcolumnExist(self.TblName[0], ColumnName)):
					print("Column name '" + str(ColumnName) + "' does not exist in '" + str(self.TblName[0]) + "' table!")
					return False
		

		 
			return True				


			print('Table name and column names have been checked!') 
			
							


	
	def SetColumnValue(Clause):
		SetColVal = {}
		for index in range(len(Clause)):			
			if Clause[index] == '=':
				SetColVal[Clause[index-1]] = Clause[index+1]
		print('Where Column Name and Value:' + str(SetColVal))
		return SetColVal		

			
		
	def MakeUpdate(self): 		
		self.DissectUpdate();
		#Val = self.CheckUpdate();
		#Val2 = self.GetPrimaryKey();
		#if Val == True: #and Val2 == True:
		#	self.PerformUpdate();
			
			

	def GetPrimaryKey(self):
	
		#This Function will Get the Primary key of matched condition from where clause
		
		CSVFile = open(self.TblName[0]+".csv")
		AllRecords = CSVFile.readlines()
		CSVFile.close()
		lTableAllColNames = meta.getAllColumns(self.TblName[0]) # Get all the Columns names of Given Tables
		#PrimaryKey = []
		#print('AllRecords: ' + str(AllRecords))
		
		#get the index of the column names of the table to be searched
		iSearchIndex = [] # Index will be assigned to list of integer
		for ColumnName in self.WhereColName:
			iSearchIndex.append(lTableAllColNames.index(str(ColumnName)))
			
		# Start the Searching of Table ID by extracting each record and compare with the where values	
		for lRecord in AllRecords:
			lRecord = lRecord.lower() # Lower all the character
			lRecord = lRecord.replace("\n","") # Remove \new line
			lSplitRecord = lRecord.split(',') # Split the records list
			
			iColValIndex = 0	# this Index will be used by self.WhereColVal list
			blnTFCounter = [] # List that will collect  True and False evaluation of the search fields
			iRecordId = lSplitRecord[0] # initialized the Record ID of each tuple
			
			# Dito Magsisimula mag navigate for each record
			for Index in iSearchIndex:			
				#for compare in self.WhereComOperator:
				if self.WhereComOperator[iColValIndex] == '=' :
						#Value from record         Value from wherecolvalue
					if lSplitRecord[Index] == self.WhereColVal[iColValIndex]:
							
						print('iRecordId:' + str(iRecordId))
						print('Index and iColValIndex ' + str(Index) + ':' + str(iColValIndex))								
						blnTFCounter.append(True)
						print('blnTFCounter' + str(blnTFCounter))				
					elif lSplitRecord[Index] != self.WhereColVal[iColValIndex]:
						blnTFCounter.append(False)
						
				#iColValIndex =iColValIndex + 1
			
				#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
					
				elif self.WhereComOperator[iColValIndex] == '<':
					if lSplitRecord[Index] < self.WhereColVal[iColValIndex]:
						blnTFCounter.append(True)
					else: 
						blnTFCounter.append(False)
				#iColValIndex =iColValIndex + 1
				
				elif self.WhereComOperator[iColValIndex] == '>':
					if lSplitRecord[Index] > self.WhereColVal[iColValIndex]:
						blnTFCounter.append(True)
					else:
						blnTFCounter.append(False)
				#iColValIndex =iColValIndex + 1
				
				elif self.WhereComOperator[iColValIndex] == '!=':
					if lSplitRecord[Index] != self.WhereColVal[iColValIndex]:
						blnTFCounter.append(True)
					else:
						blnTFCounter.append(False)	
						
				iColValIndex =iColValIndex + 1
						
				
			# Dito mag start mag compare all the collected True and False from blnTFCounter using value form self.WhereLogicOperator
			if len(self.WhereLogicOperator) != 0:
				for Index in range(len(self.WhereLogicOperator)):
					blnResult = "" #Boolean Variable that will hold the result blnTFCounter Collected True or False
				
					if blnResult == "":
						if self.WhereLogicOperator[Index] == 'and':
							blnResult = blnTFCounter[Index] and blnTFCounter[Index + 1]
						elif  self.WhereLogicOperator[Index] == 'or':
							blnResult = blnTFCounter[Index] or blnTFCounter[Index + 1]
					else:
						if self.WhereLogicOperator[Index] == 'and':
							blnResult = blnTFCounter[Index] and blnTFCounter[Index + 1]
						elif  self.WhereLogicalOperator[Index] == 'or':
							blnResult = blnTFCounter[Index] or blnTFCounter[Index + 1]
			else:
				blnResult = "" 
				blnResult = blnTFCounter[0]
			
			
						
			if blnResult == True:
				self.PrimaryKey.append(iRecordId)
			
			#print('Result :'+ str(blnResult))	
				

														
				
		print('Primary Keys:' + str(self.PrimaryKey)) 		
		
		
	
		#print('Print All Record:' + str(AllRecords))	
		
		if len(self.PrimaryKey) == 0:
			print('Record Not Found')
			return False
		else:
			return True
			
	def PerformUpdate(self):
		
		CSVFile = open(self.TblName[0]+".csv")
		AllRecords = CSVFile.readlines()
		CSVFile.close()
		TableAllColNames = meta.getAllColumns(self.TblName[0]) # Get all the Columns names of Given Tables
		
		for Record in AllRecords:
			SplitRecord = Record.split(',') # Split the Record to extract PK
			if SplitRecord[0] == self.PrimaryKey[0]: # Compare and Search PK
				RecordIndex = AllRecords.index(Record) #Get the Record index from AllRecords
				#print('Record Found!:' + str(Record))
				#print('Split Record!:' + str(SplitRecord)) 
				#print('Record:' + str(AllRecords[RecordIndex]))
				#+++++++++++++++++++++++++++++++++++++++++++++++++++++
				for index in range(len(self.SetColNameToUpdate)):
					UpdateIndex = TableAllColNames.index(str(self.SetColNameToUpdate[index]))
					Domain = self.SetColValToUpdate[index]
					SplitRecord[UpdateIndex] = Domain.replace("'","")
					
				#print('Updated SplitRecord' + str(SplitRecord))
				UpdateRecord = ""
				for field in SplitRecord:
					if '\n' not in field:
						UpdateRecord = UpdateRecord + str(field + '\n') #Fill out the UpdateRecord String
					else:
						UpdateRecord = UpdateRecord + str(field)
				
				UpdateRecord = UpdateRecord.replace('\n',',',len(SplitRecord)-1) # Replace '\n' with commas(,)
	
				print('Update Record: ' + UpdateRecord)	
				
				#++++++++++++++++++++++++++++++++++++++++	
				
				AllRecords[RecordIndex]=str(UpdateRecord) #Insert the Update in AllRecords
				break
		
		#print('Display all records:' + str(AllRecords))
		
		CSV_Output = open(self.TblName[0]+"All.csv","w")
		for Record in AllRecords:
			CSV_Output.write(str(Record))
		CSV_Output.close()
		print('One Row has been Updated!')
		
'''			
	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Delete
	def perform_operations(self):
		result=[]
		self.counter=0
		statement=''
		print(self.targetPrint)
		if len(self.where_operation) == 0:
			print("No where operation")
			for i in range(0,len(self.targetPrint)):
				if self.targetPrint[i]=='*':
					print("print ALL")
					Data.PrintDataALL(self.tblname,self.database)
				else:
					print("columns")
					Data.PrintColumn(self.tblname,self.targetPrint,self.database)


		#for i in range (0,len(self.where_operation)):
		#	print("ops ",self.where_operation[i],"--->type ",type(self.where_operation[i]))
=======+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def PerformUpdate(self): # Do not delete
		self.fetch_data()
		self.GetPK()
		#perform operations pass the list of operations
		#returns list of primary key + data
		#prints it

		
		
	
	def fetch_data(self): # Do not Delete
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
	
'''	

	
