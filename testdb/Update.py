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
		
		
	def HelloUpdate(self):
		print ('HELLO UPDATE, This is where we start!')
		
		
