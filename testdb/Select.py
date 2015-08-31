from Select import * 
from FileReader import *
from Metadata import *
class Select:

	def __init__(self,statements,database):
	
		self.statementList = statements;
		self.data =[];
		self.meta = Metadata();
		self.qlength = len(statements);
		self.database = database;

	def make_select(self):
		
		self.check_show();

	#def buildTree(self):
		
		
	def check_show(self):
		for i in range(1,(len(self.statementList))):			
			if(self.statementList[i]=="*"):
				if (self.meta).checkTableExist(self.statementList[i+1]):
					filer=FileReader(self.statementList[i+1])						
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
	
		
	
		
  
		
