'''
CMSC 227 1ST Sem SY 2015 - 2016 
UPDATE Class
Wenceslao Navallo
Venus Retuya


'''


from Update import * 
from FileReader import *
from Metadata import *
import datetime 

class Update:

	def __init__(self,statements,database):	
		self.statementList = statements;
		self.data =[];
		global meta
		meta = Metadata();
		self.qlength = len(statements);
		self.database = database;
		

	
	def DissectUpdate(self):
		# This function will dissect the Update statement will be saved to the following variable set
		
		self.TblName = [];
		self.PrimaryKey = [];
		self.SetColNameToUpdate = [];
		self.SetColValToUpdate =[];
		self.WhereColName = [];
		self.WhereColVal = [];
		self.WhereComOperator = [];
		self.WhereLogicOperator = [];
		
		
		lUpdateStatement = self.statementList
		#print('Update Statement:' + str(lUpdateStatement))
		
		#get Table Name
		self.TblName.append(self.statementList[1])
		#print('Table Name:' + str(self.TblName))
		
		#Dissect SET and WHERE CLAUSE 
		
		if 'where' in lUpdateStatement:
			
			#SET CLAUSE
			iSetIndex = lUpdateStatement.index('set') # get the index of 'set'
			iWhereIndex = lUpdateStatement.index('where')  # get the index of 'where'
		
			lSetClause = lUpdateStatement[iSetIndex+1:iWhereIndex] # extract the set clause
			
		
			#Iterate to SetClause and assign the Column name and its value to self 
			for Index in range(len(lSetClause)):				
				if lSetClause[Index] == '=':
					self.SetColNameToUpdate.append(lSetClause[Index - 1])
					self.SetColValToUpdate.append(lSetClause[Index + 1].replace("'",""))	
				
			#print('Set Column Name:' + str(self.SetColNameToUpdate))
			#print('Set Column Value:' + str(self.SetColValToUpdate))		 
		
			#WHERE CLAUSE
			lWhereClause = lUpdateStatement[iWhereIndex+1:len(lUpdateStatement)] # extract the where clause
			
			#Comparison Operators
			lCompareOperator =['=','!=','>','<'];
			
			#LogicalOperator
			lLogicalOperator = ['and','or'];
			
			#Iterate to Where Clause and assign the Column names and its value, comparison and logical operators to self 	
			for Index in range(len(lWhereClause)):			
				if lWhereClause[Index] in lCompareOperator:
					self.WhereComOperator.append(lWhereClause[Index])
					self.WhereColName.append(lWhereClause[Index-1]) 
					self.WhereColVal.append(lWhereClause[Index+1].replace("'",""))
				else:
					if lWhereClause[Index] in lLogicalOperator:
						self.WhereLogicOperator.append(lWhereClause[Index])
						
			self.WhereColVal = self.WhereConvertDataType(self.WhereColVal) #perform the Convertion of clause
			
			#For trouble shooting	
			#print('Where Column Name :' + str(self.WhereColName))
			#print('Where Comparison Operator:' + str(self.WhereComOperator))
			#print('Where Column Value:' + str(self.WhereColVal))
			#print('Where Logical Operator:' + str(self.WhereLogicOperator))
			
			
			
		else:
			#Update statement without Where Clause
			iSetIndex = lUpdateStatement.index('set')
			lSetClause = lUpdateStatement[iSetIndex+1:len(lUpdateStatement)]
		
			#Iterate to SetClause and assign the Column name and Value to self
			for Index in range(len(lSetClause)):				
				if lSetClause[Index] == '=':
					self.SetColNameToUpdate.append(lSetClause[Index - 1])
					self.SetColValToUpdate.append(lSetClause[Index + 1])
								
			print('Set Column Name:' + str(self.SetColNameToUpdate))
			print('Set Column Value:' + str(self.SetColValToUpdate))
			
		

	def CheckUpdate(self):
		
		#This function will check the existence of tables and column in data dictionary or metadata
		
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


	def GetPrimaryKey(self):
	
		#This Function will Search and Get the Primary key of matched condition of the table to update and  where clause
		
		CSVFile = open(self.TblName[0]+".csv")
		AllRecords = CSVFile.readlines()
		CSVFile.close()
		lTableAllColNames = meta.getAllColumns(self.TblName[0]) # Get all the Columns names of Given Tables
		lTableDataType = meta.getAllDatatypes(self.TblName[0]) # Get all the Data Type of Column names
		#PrimaryKey = []
		#print('AllRecords: ' + str(AllRecords))
		
		#get the index of the column names of the table to be searched
		iSearchIndex = [] # Index will be assigned to list of integer
		for ColumnName in self.WhereColName:
			iSearchIndex.append(lTableAllColNames.index(str(ColumnName)))
			
		# Start the Searching of Table ID by extracting each record and compare with the where values	
		for lRecord in AllRecords:
			lRecord = lRecord.lower() # Lower all the character
			lRecord = lRecord.replace("\n","") # Remove \new lineS
			lSplitRecord = lRecord.split(',') # Split the records list
			
			# Perform the conversion of tuples' Data Types
			lSplitRecord = self.RowConvertDataType(lSplitRecord)
			
			iColValIndex = 0	# this Index will be used by self.WhereColVal list
			blnTFCounter = [] # List that will collect  True and False evaluation of the search fields
			iRecordId = str(lSplitRecord[0]) # initialized the Record ID of each tuple and convert it to string from interger 
			
			# Dito Magsisimula mag navigate for each record
			for Index in iSearchIndex:			
				#for compare in self.WhereComOperator:
				if self.WhereComOperator[iColValIndex] == '=' :
						#Value from record         Value from wherecolvalue
					if lSplitRecord[Index] == self.WhereColVal[iColValIndex]:						
						#print('iRecordId:' + str(iRecordId))
						#print('Index and iColValIndex ' + str(Index) + ':' + str(iColValIndex))								
						blnTFCounter.append(True)
						#print('blnTFCounter' + str(blnTFCounter))				
					elif lSplitRecord[Index] != self.WhereColVal[iColValIndex]:
						blnTFCounter.append(False)
						
				#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
					
				elif self.WhereComOperator[iColValIndex] == '<':
					if lSplitRecord[Index] < self.WhereColVal[iColValIndex]:
						blnTFCounter.append(True)
					else: 
						blnTFCounter.append(False)
								
				elif self.WhereComOperator[iColValIndex] == '>':
					if lSplitRecord[Index] > self.WhereColVal[iColValIndex]:
						blnTFCounter.append(True)
					else:
						blnTFCounter.append(False)
				
				
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
			
			# When the evaluation of the Record is completed the id will be appended to PK
			if blnResult == True:
				self.PrimaryKey.append(iRecordId) #Record(s) to update!
			
			#print('Result :'+ str(blnResult))	
		
		if len(self.PrimaryKey) == 0:
			print('Record Not Found!')
			return False
		else:
			#print('Number of Primary Keys:'+str(len(self.PrimaryKey)) +':' + str(self.PrimaryKey) )
			return True
			
	def PerformUpdate(self):
		# Perform Update function will execute the update given the valid collected ID or PK passed by GetPrimaryKey function 
		
		CSVFile = open(self.TblName[0]+".csv")
		AllRecords = CSVFile.readlines()
		CSVFile.close()
		TableAllColNames = meta.getAllColumns(self.TblName[0]) # Get all the Columns names of Given Tables
		
		for PK in self.PrimaryKey:
		
			for Record in AllRecords:
				SplitRecord = Record.split(',') # Split the Record to extract PK
				if SplitRecord[0] == PK: # Compare and Search PK
					RecordIndex = AllRecords.index(Record) #Get the Record index from AllRecords
					#for trouble shooting
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
				
					#+++++++++++++++++++++++++++++++++++++++++++++++++++++	
				
					AllRecords[RecordIndex]=str(UpdateRecord) #Insert the Update in AllRecords
					break
		
			#print('Display all records:' + str(AllRecords))
		
		CSV_Output = open(self.TblName[0]+"UPDATE.csv","w")
		for Record in AllRecords:
			CSV_Output.write(str(Record))
		CSV_Output.close()
		
		print('Query OK, '+ str(len(self.PrimaryKey))+' row(s) affected')
		print('Row(s) Matched: ' + str(len(self.PrimaryKey)) +' Changed: ' + str(len(self.PrimaryKey)))


	def RowConvertDataType(self,Record):
		# This Function will convert 
		lTableAllColNames = meta.getAllColumns(self.TblName[0]) # Get all the Columns names of Given Tables
		lColumnDataType = meta.getAllDatatypes(self.TblName[0]) # Get equivalent Data Types of each Column
		NewRecordType = []
		Index = 0
		for Field in Record:
			if lColumnDataType[Index] == "int" :
				NewRecordType.append(int(Field))
			elif lColumnDataType[Index] == "numeric" :
				NewRecordType.append( float(Field))
			elif lColumnDataType[Index] == "varchar" : 
				NewRecordType.append( str(Field))
			elif lColumnDataType[Index] == "date" :
				NewRecordType.append(self.strToDateObj(Field)) # Use the Created function for date converstion	
			Index = Index + 1
		#print('New Record Type: ' + str(NewRecordType))
		return NewRecordType	
	
	def WhereConvertDataType(self,WhereColValue):
		# This Function Convert the Values of Where Condition saved in self.WhereColValue
		lTableAllColNames = meta.getAllColumns(self.TblName[0]) # Get all the Columns names of Given Tables
		lColumnDataType = meta.getAllDatatypes(self.TblName[0]) # Get equivalent Data Types of each Column
		NewWhereValueType = []
		Index = 0
		for Value in WhereColValue :
			if lColumnDataType[lTableAllColNames.index(self.WhereColName[Index])] == "int" :
				NewWhereValueType.append(int(Value))
			elif lColumnDataType[lTableAllColNames.index(self.WhereColName[Index])] == "numeric" :
				NewWhereValueType.append(float(Value))
			elif lColumnDataType[lTableAllColNames.index(self.WhereColName[Index])] == "varchar" :
				NewWhereValueType.append(str(Value))
			elif lColumnDataType[lTableAllColNames.index(self.WhereColName[Index])] == "date" :
				NewWhereValueType.append(self.strToDateObj(Value))	
			Index = Index + 1
		#print('NewWhereValueType:' + str(NewWhereValueType))		
		return NewWhereValueType

	def strToDateObj(self, dString):
		# Function that converts String to Date Object
		lDateStr = dString.split("-")
		lDateStr.reverse()
		iYear = int(lDateStr[0])
		iMonth = int(lDateStr[1])
		iDay = int(lDateStr[2])
		DateObj = datetime.date(iYear,iMonth,iDay)
		#print(str(DateObj))
		#returns Date Object
		return DateObj
		
	
	def objDateToString(self, DateObj):
		#Function that Converts Date Object to String
		
		StrDate = str(DateObj) # Date obj To String
		#StrDate = StrDate.replace("-","/")
		#print(StrDate)
		StrDate = StrDate.split("-")
		StrDate.reverse()
		sDate = ""
		for date in StrDate:
			sDate = sDate + str(date)+"-"
		#returns String Date		
		return sDate.strip("-")

	
	
		
	def MakeUpdate(self): 		
		self.DissectUpdate();
		Val = self.CheckUpdate();
		if Val == True:
			Val2 = self.GetPrimaryKey();
		if Val == True and Val2 == True:
			self.PerformUpdate();

		

	
