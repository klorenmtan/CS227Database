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
		
	def UpdateTree(self):
		self.TblName = [];
		self.PrimaryKey = [];
		self.SetColNameToUpdate = [];
		self.SetColValToUpdate = [];
		self.WhereColName = [];
		self.WhereColVal = [];
						
				
		lUpdateStatement = self.statementList
		iTable = lUpdateStatement.index('update')
		iSet = lUpdateStatement.index('set')
		iWhere = lUpdateStatement.index('where') 
		#print('From ' + str(iSet) + ' To' + str(iWhere))
		
		
		#get Table Name
		#self.TblName = self.statementList[1]
		#print('Table Name:' + self.TblName)
		UpdateSet = lUpdateStatement [iTable+1: iSet]
		self.TblName = str(UpdateSet)		
		print ('Table Name(s):' + self.TblName)
				
		
		#get Set Column Name to update and its value
		SetWhere = lUpdateStatement[iSet+1:iWhere]
		strSetWhere = str(SetWhere)
		iSetCol = strSetWhere.split('=')
		self.SetColNameToUpdate = iSetCol[0];
		self.SetColValToUpdate = iSetCol[1];
		print ('Set Column Name(s):' + (self.SetColNameToUpdate))
		print ('Set Column Value(s):' + (self.SetColValToUpdate))
		#print('Set Column Name and Value:' + str(SetWhere))
		
		
		#get where Column Name and its value		
		AfterWhere = lUpdateStatement[iWhere+1:len(lUpdateStatement)]
		strAfterWhere = str(AfterWhere)
		iWhereCol = strAfterWhere.split('=')
		self.WhereColName = iWhereCol[0];
		self.WhereColVal = iWhereCol[1];
		print ('Where Column Name(s):' + (self.WhereColName))
		print ('Where Column Value(s):' + (self.WhereColVal))
		#print('Where Column Name and Value:' + str(AfterWhere))'''
		
		#check if the table is existing				
		if not (meta.checkTableExist(self.TblName)):
			print('Table Does Not Exist')
			return False
		else:
			if not (meta.checkTableExist(self.SetColNameToUpdate)):
				print('Set Column Name Does Not Exist')
				return False
		
		
		
	def makeUpdate(self): 
		val=self.UpdateTree()
		if val==True:		
			self.performUpdate()	
			
	def performUpdate(self):
		self.fetch_data()
		self.perform_operations()
		#perform operations pass the list of operations
		#returns list of primary key + data
		#prints it
			
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
	
	def fetch_data(self):
		array1 = {}
		
		for i in range(0,len(self.tblname)):
			if not(self.tblname[i] in self.database.keys()):
				filer=FileReader(self.tblname[i])
				filer.fileRead()
				array1=filer.hashData()
				self.database[self.tblname[i]]=array1
				

		print(self.database.keys())
	
	
	def HelloUpdate(self):
		print ('HELLO UPDATE, This is where we start!')
		print(self.statementList)
		print(self.qlength)
		
		
