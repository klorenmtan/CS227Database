#UPDATE Class
#Venus Retuya
#Wens Navallo
#

from Update import * 
#from FileReader import *
#from Metadata import *
class Update:

	def __init__(self,statements,database):
	
		self.statementList = statements;
		self.data =[];
		#global meta
		#meta = Metadata();
		self.qlength = len(statements);
		self.database = database;
	
	def UpdateTree(self):
		self.TblName = [];
		self.PrimaryKey = [];
		self.SetColNameToUpdate = [];
		self.SetValToUpdate =[];
		self.WhereColName = [];
		self.WhereColVal = [];
		
		#get Table Name
		self.TblName = self.statementList[1]
		print('Table Name:' + self.TblName)
		
		#get Set Column Name to update and its value
		lUpdateStatement = self.statementList
		iSet = lUpdateStatement.index('set')
		iWhere = lUpdateStatement.index('where') 
		#print('From ' + str(iSet) + ' To' + str(iWhere))
		
		
		SetWhere = lUpdateStatement[iSet+1:iWhere]
		print('Set Column Name and Value:' + str(SetWhere))
		
		AfterWhere = lUpdateStatement[iWhere+1:len(lUpdateStatement)]
		print('Where Column Name and Value:' + str(AfterWhere))
		
		

		
	
		
		
		
		
		#get where Column Name and its value
		
		
	def HelloUpdate(self):
		print ('HELLO UPDATE, This is where we start!')
		print(self.statementList)
		print(self.qlength)
		
		
