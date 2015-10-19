from Select import * 
from FileReader import *
from Delete import *
from Update import *
class Query:
	def __init__(self,query,database):
		self.query = query
		self.database = database

	def classify_query(self):
		stat = (self.query).split("|");
		self.operation = stat[0]
		if(self.operation=="select"):
			print(stat)
			q1=Semantic(stat,"select")
			check=q1.select_tree()
			
		
			if check == True:
				tblnames=q1.returnTblname()
				targetPrint=q1.returnTargetPrint()
				join_clause=q1.returnJoinClause()
				where_operation=q1.returnWhere()
				query1 = Select(stat,self.database,targetPrint,tblnames,join_clause,where_operation)
				query1.make_select()
			else:
				return False	

		if(self.operation=="update"):
			print(stat)
			q1=Semantic(stat,"update")
			check=q1.select_tree()

			if check == True:
				targetColumns=q1.returnColumns()
				newValues=q1.returnNewValues()
				tblnames=q1.returnTblname()
				where_operation=q1.returnWhere()
				query1 = Update(stat,self.database,targetColumns,tblnames,newValues,where_operation)
				self.database=query1.perform_update()
						
					
		
		if(self.operation=="delete"):	
			q1=Semantic(stat,"delete")
			check=q1.select_tree()

			if check==True:
				tblname = q1.returnTblname()
				where_operation=q1.returnWhere()
				query1=Delete(stat,self.database,tblname,where_operation)
				self.database=query1.perform_delete()				
		
	
	


