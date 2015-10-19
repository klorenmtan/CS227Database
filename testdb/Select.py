from Select import * 
from FileReader import *
from Metadata import *
from Semantic import *
import time
import datetime
class Select:

	def __init__(self,statements,database,targetPrint,tblname,joinClause,whereOperation):
	
		self.statementList = statements;
		self.data =[];
		global meta
		meta = Metadata();
		self.qlength = len(statements);
		self.database = database;
		self.targetPrint=targetPrint
		self.tblname=tblname
		self.join_clause=joinClause
		self.where_operation=whereOperation
	
		
	def make_select(self): 
		self.perform_select()

	def perform_select(self):
		self.fetch_data()
		self.perform_operations()
		
	def perform_operations(self):
		result=[]
		r1=[]
		self.counter=0
		statement=''
		#print(self.targetPrint)
		if len(self.where_operation) == 0 and len(self.join_clause)==0:				#simple select
			#print("No where operation")
			if self.targetPrint[0]=='*':
				result=Data.PrintDataALL(self.tblname,self.database)
				
			else:
				result=Data.PrintColumn(self.tblname,self.targetPrint,self.database)
			Data.printData(result,self.tblname,self.targetPrint)
			if len(result) == 1:
				print(len(result),"row returned")
			else:
				print(len(result),"rows returned")

		elif len(self.where_operation) == 0 and len(self.join_clause)!=0:			#select with join
						
			columns=[]

			result=Data.PrintDataALL(self.tblname,self.database)
			
			print(self.join_clause)				
			for j in range(0,len(self.tblname)):
				columns.extend(meta.getAllColumns(self.tblname[j]))
			
			r1=Select.classify_where(self.tblname,self.join_clause,result,columns)			
			if self.targetPrint[0]=='*':
				Data.printData(r1,self.tblname,self.targetPrint)												
			else:	
				Data.printDataWhere(r1,self.tblname,self.targetPrint,columns)
			if len(r1) == 1:
				print(len(r1),"row returned")
			else:
				print(len(r1),"rows returned")
			
		elif len(self.where_operation) !=0 and len(self.join_clause)!=0:			#select with join and where
			columns=[]			
			result=Data.PrintDataALL(self.tblname,self.database)
			for j in range(0,len(self.tblname)):
				columns.extend(meta.getAllColumns(self.tblname[j]))

			r1=Select.classify_where(self.tblname,self.join_clause,result,columns)
			r2=Select.classify_where(self.tblname,self.where_operation,r1,columns)

			if self.targetPrint[0]=='*':
				Data.printData(r2,self.tblname,self.targetPrint)												
			else:	
				Data.printDataWhere(r2,self.tblname,self.targetPrint,columns)
			if len(r2) == 1:
				print(len(r2),"row returned")
			else:
				print(len(r2),"rows returned")

						

		elif len(self.where_operation) != 0 and len(self.join_clause) == 0:			#select with where
			columns=[]
			
			result=Data.PrintDataALL(self.tblname,self.database)
			#print(self.where_operation)				
			for j in range(0,len(self.tblname)):
				columns.extend(meta.getAllColumns(self.tblname[j]))
			
			r1=Select.classify_where(self.tblname,self.where_operation,result,columns)			
			if self.targetPrint[0]=='*':
				Data.printData(r1,self.tblname,self.targetPrint)												
			else:	
				Data.printDataWhere(r1,self.tblname,self.targetPrint,columns)
			if len(r1) == 1:
				print(len(r1),"row returned")
			else:
				print(len(r1),"rows returned")

	def checkMatch(tblname,typeop,column,data,datahash,index):
		
		results=[]
		#meta.getAllColumns(tblname)
		meta=Metadata()
		columns=[]
		fcol=[]
		datatypes=[]
		fdatatypes=[]
		for i in range(0,len(tblname)):
			columns=meta.getAllColumns(tblname[i])		
			fcol=fcol+columns
			datatypes=meta.getAllDatatypes(tblname[i])
			fdatatypes=fdatatypes+datatypes

		
		if typeop == 1:
			for i in range(0,len(datahash)):
				index1=fcol.index(column)
				
				if fdatatypes[index1] == "int":
					if datahash[i][index1] < int(data):
						results.append(datahash[i])

				elif fdatatypes[index1] == "numeric":
					if datahash[i][index1] < float(data):
						results.append(datahash[i])

				elif fdatatypes[index1] == 'varchar':
					print("Can't compare strings!")

				elif fdatatypes[index1] == 'date':
					date1=str(datahash[i][index1])
					date2=str(data);
					newdate1 = time.strptime(date1,'%d-%m-%Y')
					newdate2 = time.strptime(date2,'%d-%m-%Y')
					if newdate1 < newdate2:
						results.append(datahash[i])
			
		elif typeop == 2:
			for i in range(0,len(datahash)):
				index1=fcol.index(column)
				
				if fdatatypes[index1] == "int":
					if datahash[i][index1] > int(data):
						results.append(datahash[i])

				elif fdatatypes[index1] == "numeric":
					if datahash[i][index1] > float(data):
						results.append(datahash[i])

				elif fdatatypes[index1] == 'varchar':
					print("Can't compare strings!")

				elif fdatatypes[index1] == 'date':
					date1=str(datahash[i][index1])
					date2=str(data);
					newdate1 = time.strptime(date1,'%d-%m-%Y')
					newdate2 = time.strptime(date2,'%d-%m-%Y')
					if newdate1 > newdate2:
						results.append(datahash[i])
		
				
	
		if typeop == 3:
			for i in range(0,len(datahash)):
				index1=fcol.index(column)
				
				if fdatatypes[index1] == "int":
					if datahash[i][index1] == int(data):
						results.append(datahash[i])

				elif fdatatypes[index1] == "numeric":
					if datahash[i][index1] == float(data):
						results.append(datahash[i]) 

				elif fdatatypes[index1] == 'varchar':
					if datahash[i][index] == str(data):
						results.append(datahash[i])

				elif fdatatypes[index1] == 'date':
					date1=str(datahash[i][index1])
					date2=str(data);
					newdate1 = time.strptime(date1,'%d-%m-%Y')
					newdate2 = time.strptime(date2,'%d-%m-%Y')
					if newdate1 == newdate2:
						results.append(datahash[i])

		elif typeop == 4:
			for i in range(0,len(datahash)):
				index1=fcol.index(column)
				
				if fdatatypes[index1] == "int":
					if datahash[i][index1] != int(data):
						results.append(datahash[i])

				elif fdatatypes[index1] == "numeric":
					if datahash[i][index1] != float(data):
						results.append(datahash[i]) 

				elif fdatatypes[index1] == 'varchar':
					if datahash[i][index] != str(data):
						results.append(datahash[i])

				elif fdatatypes[index1] == 'date':
					date1=str(datahash[i][index1])
					date2=str(data);
					newdate1 = time.strptime(date1,'%d-%m-%Y')
					newdate2 = time.strptime(date2,'%d-%m-%Y')
					if newdate1 != newdate2:
						results.append(datahash[i])
		

		
		return results


	def checkMatch2(tblname,typeop,column,data,datahash,index,j):

		results=[]
		#meta.getAllColumns(tblname)
		columns=[]
		fcol=[]
		datatypes=[]
		fdatatypes=[]
		for i in range(0,len(tblname)):
			columns=meta.getAllColumns(tblname[i])		
			fcol=fcol+columns
			datatypes=meta.getAllDatatypes(tblname[i])
			fdatatypes=fdatatypes+datatypes

		
		if typeop == 1:
			for i in range(0,len(datahash)):
				if i==j:
					index1=fcol.index(column)
				
					if fdatatypes[index1] == "int":
						if datahash[i][index1] < int(data):
							results.append(datahash[i])

					elif fdatatypes[index1] == "numeric":
						if datahash[i][index1] < float(data):
							results.append(datahash[i])

					elif fdatatypes[index1] == 'varchar':
						print("Can't compare strings!")

					elif fdatatypes[index1] == 'date':
						date1=str(datahash[i][index1])
						date2=str(data);
						newdate1 = time.strptime(date1,'%d-%m-%Y')
						newdate2 = time.strptime(date2,'%d-%m-%Y')
						if newdate1 < newdate2:
							results.append(datahash[i])
			
		elif typeop == 2:
			for i in range(0,len(datahash)):
				index1=fcol.index(column)
				if i==j:
					if fdatatypes[index1] == "int":
						if datahash[i][index1] > int(data):
							results.append(datahash[i])

					elif fdatatypes[index1] == "numeric":
						if datahash[i][index1] > float(data):
							results.append(datahash[i])

					elif fdatatypes[index1] == 'varchar':
						print("Can't compare strings!")

					elif fdatatypes[index1] == 'date':
						date1=str(datahash[i][index1])
						date2=str(data);
						newdate1 = time.strptime(date1,'%d-%m-%Y')
						newdate2 = time.strptime(date2,'%d-%m-%Y')
						if newdate1 > newdate2:
							results.append(datahash[i])
		
				
	
		if typeop == 3:
			for i in range(0,len(datahash)):
				index1=fcol.index(column)
				if i==j:
					if fdatatypes[index1] == "int":
						if datahash[i][index1] == int(data):
							results.append(datahash[i])

					elif fdatatypes[index1] == "numeric":
						if datahash[i][index1] == float(data):
							results.append(datahash[i]) 

					elif fdatatypes[index1] == 'varchar':
						if datahash[i][index] == str(data):
							results.append(datahash[i])

					elif fdatatypes[index1] == 'date':
						date1=str(datahash[i][index1])
						date2=str(data);
						print(date1,date2)
						newdate1 = time.strptime(date1,'%d-%m-%Y')
						newdate2 = time.strptime(date2,'%d-%m-%Y')
						if newdate1 == newdate2:
							results.append(datahash[i])

		elif typeop == 4:
			for i in range(0,len(datahash)):
				index1=fcol.index(column)
				if i==j:
					if fdatatypes[index1] == "int":
						if datahash[i][index1] != int(data):
							results.append(datahash[i])

					elif fdatatypes[index1] == "numeric":
						if datahash[i][index1] != float(data):
							results.append(datahash[i]) 

					elif fdatatypes[index1] == 'varchar':
						if datahash[i][index] != str(data):
							results.append(datahash[i])

					elif fdatatypes[index1] == 'date':
						date1=str(datahash[i][index1])
						date2=str(data);
						
						newdate1 = time.strptime(date1,'%d-%m-%Y')
						newdate2 = time.strptime(date2,'%d-%m-%Y')
						if newdate1 != newdate2:
							results.append(datahash[i])

		return results
	def getIndex(columns,operation):	
		
		for i in range(0,len(columns)):
			if operation== columns[i]:
				return i
		return -1

	def classify_where(tblname,operation,datahash,columns):
		pk=[]		
		result=[]		
		index=[]
		a=[]		
		if len(operation) == 3:
			#print("single where")		
			
			if type(operation[2]) == str:
				val=Select.getIndex(columns,operation[2])	
				if val == -1:
					if operation[1] == '<':
						result=Select.checkMatch(tblname,1,operation[0],operation[2],datahash,Select.getIndex(columns,operation[0]))
					elif operation[1] == '>':
						result=Select.checkMatch(tblname,2,operation[0],operation[2],datahash,Select.getIndex(columns,operation[0]))
					elif operation[1] == '=':
						#print("index",Select.getIndex(columns,operation[0]))
						result=Select.checkMatch(tblname,3,operation[0],operation[2],datahash,Select.getIndex(columns,operation[0]))
					elif operation[1] == '!=':
						
						#print("index",Select.getIndex(columns,operation[0]))
						result=Select.checkMatch(tblname,4,operation[0],operation[2],datahash,Select.getIndex(columns,operation[0]))
					#print("HEHR")
				else:
						if operation[1] == '<':
							for i in range(0,len(datahash)):
								b=Select.getIndex(columns,operation[2])
								a=Select.checkMatch2(tblname,1,operation[0],datahash[i][b],datahash,Select.getIndex(columns,operation[0]),i)
								result.extend(a)
						elif operation[1] == '>':
							for i in range(0,len(datahash)):
								b=Select.getIndex(columns,operation[2])
								a=Select.checkMatch2(tblname,2,operation[0],datahash[i][b],datahash,Select.getIndex(columns,operation[0]),i)		
								result.extend(a)
						elif operation[1] == '=':
							for i in range(0,len(datahash)):
								b=Select.getIndex(columns,operation[2])
								a=Select.checkMatch2(tblname,3,operation[0],datahash[i][b],datahash,Select.getIndex(columns,operation[0]),i)											
								result.extend(a)
						elif operation[1] == '!=':
								b=Select.getIndex(columns,operation[2])
								a=Select.checkMatch2(tblname,4,operation[0],datahash[i][b],datahash,Select.getIndex(columns,operation[0]),i)											
								result.extend(a)
			else:	
				if operation[1] == '<':
					result=Select.checkMatch(tblname,1,operation[0],operation[2],datahash,Select.getIndex(columns,operation[0]))
				elif operation[1] == '>':
					result=Select.checkMatch(tblname,2,operation[0],operation[2],datahash,Select.getIndex(columns,operation[0]))
				elif operation[1] == '=':
					result=Select.checkMatch(tblname,3,operation[0],operation[2],datahash,Select.getIndex(columns,operation[0])) 
				elif operation[1] == '!=':
					result=Select.checkMatch(tblname,4,operation[0],operation[2],datahash,Select.getIndex(columns,operation[0]))
		
								
		else:
			i=0
			count=0	
			res=[]
			res1=[]
			ans=[]
			#results=[]
			#print("complex where")
			while i < len(operation):
				if operation[i] == "and":
					if count == 0:
						ops1=operation[i-3:i]
						ops2=operation[i+1:i+4]
						res=Select.classify_where(tblname,ops1,datahash,columns)
						res1=Select.classify_where(tblname,ops2,res,columns)
						res=res1
						count=count+1
					else:
						ops1=operation[i+1:i+4]
						res1=Select.classify_where(tblname,ops1,res,columns)
						count= count+1
					#break
				elif operation[i] == "or":
					ops1=operation[i-3:i]
					ops2=operation[i+1:i+5]
					if count == 0:					
						res=Select.classify_where(tblname,ops1,datahash,columns)
						res1=Select.classify_where(tblname,ops2,datahash,columns)
												
						for i in range(0,len(res1)):
							if res1[i] not in res:
								res.append(res1[i])
							else:
								print(res1[i])
						
						
						res1=res
						count = count+1
					else:
						ops1=operation[i+1:i+4]
						res1=Select.classify_where(tblname,ops1,res,columns)
						for i in range(0,len(res1)):
							if res1[i] not in res:
								res.append(res1[i])
							else:
								print(res1[i])
						#res.extend(res1)
						res1=res
					
				i=i+1

			result=res1


		return result	


	def fetch_data(self):
		array1 = {}
		
		for i in range(0,len(self.tblname)):
			if not(self.tblname[i] in self.database.keys()):
				filer=FileReader(self.tblname[i])
				filer.fileRead()
				array1=filer.hashData()
				self.database[self.tblname[i]]=array1
				

		

				


		
  
		
