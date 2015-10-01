from Select import * 
from Update import *
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

		if(stat[0]=="update"):
			query2 = Update(stat,self.database);			
			#query2.DissectUpdate();
			query2.MakeUpdate();
			
				
		
		#if(stat[0]=="delete"):		
		
	
	


