from Select import * 
from FileReader import *
class Query:
	def __init__(self,query,database):
		self.query = query
		self.database = database

	def classify_query(self):
		stat = (self.query).split(" ");
		self.operation = stat[0]
		if(self.operation=="select"):
			query1 = Select(stat,self.database);
			query1.make_select();	

		#if(stat[0]=="update"):	
		
		#if(stat[0]=="delete"):		
		
	
	


