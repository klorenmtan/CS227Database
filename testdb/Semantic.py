from Select import * 
from FileReader import *
from Metadata import *
import datetime
class Semantic:

	def __init__(self,statements,ops):
	
		self.statementList = statements;
		self.data =[];
		global meta
		meta = Metadata();
		self.qlength = len(statements);
		self.operation = ops		


	def getTargetPrint(self):
		i=1
		while(self.statementList[i]!='from'):
			self.targetPrint.append(self.statementList[i])
			i=i+1

		return self.targetPrint

	def getTables(self):
		i=self.statementList.index('from')+1
		
		if 'natural' in self.statementList:
			while(i<len(self.statementList)):
				if self.statementList[i] == 'on' or self.statementList[i] == 'where':
					break
				elif self.statementList[i] == 'natural' or self.statementList[i] == 'join':
					i=i+1
					continue
				else:
					self.tblname.append(self.statementList[i])
					i=i+1		


		elif 'join' in self.statementList:
			while(i<len(self.statementList)):
				if self.statementList[i] == 'on':
					break
				elif self.statementList[i] == 'where':
					break
				elif self.statementList[i] == 'join':
					i=i+1
					continue
				else:
					self.tblname.append(self.statementList[i])
					i=i+1		


		elif 'where' not in self.statementList:
			while(i<len(self.statementList)):
				self.tblname.append(self.statementList[i])
				i=i+1

		elif 'where' in self.statementList:
			while(i<len(self.statementList)):
				if self.statementList[i] == 'where':
					break
				else:
					self.tblname.append(self.statementList[i])
				i=i+1

		return self.tblname
	
	def getJoinClause(self):
		if 'on' in self.statementList:
			i=self.statementList.index('on')+1
			while(i<len(self.statementList)):
				if self.statementList=='where':
					break
				if self.statementList[i] == 'and':
					self.join_clause.append(self.statementList[i])
					i=i+1
					continue
				else:
					self.join_clause.append(self.statementList[i])
					i=i+1

		
		return self.join_clause
	
	def getWhere(self):
		
		if 'where' in self.statementList:
			i=self.statementList.index('where')+1
			while(i<len(self.statementList)):
				self.where_operation.append(self.statementList[i])
				i=i+1
		
		return self.where_operation				

	def checkValidTargetPrint(self):
		columns=[]
		col=[]	
		
		if len(self.targetPrint) == 1 and self.targetPrint[0] == '*':
			return True
		else:
			for i in range(0,len(self.tblname)):
				columns=meta.getAllColumns(self.tblname[i])
				columns=col+columns
				col=columns
			
			for i in range(0,len(self.targetPrint)):
				if self.targetPrint[i] not in columns:
					print(self.targetPrint[i],"Invalid Column")
					return False

			return True			
					
	
	def checkValidTables(self):
		tables=[]
		tables=meta.getAllTableName()
		for i in range(0,len(self.tblname)):
			if self.tblname[i] not in tables:
				print(self.tblname[i]," table not Found")
				return False
		return True

	def checkValidJoin(self):
		col=[]
		columns=[]

		datatype=[]
		dat=[]
		
		for i in range(0,len(self.tblname)):
			columns=meta.getAllColumns(self.tblname[i])
			datatypes=meta.getAllDatatypes(self.tblname[i])			
			columns=col+columns
			col=columns
			datatypes=dat+datatypes
			dat=datatypes
		
				
		for i in range(0,len(self.join_clause)):
			if self.join_clause[i] == 'and' or self.join_clause[i] == 'or':
				continue
			elif self.join_clause[i] in columns:
				continue
			elif self.join_clause[i] == '<' or self.join_clause[i] == '>' or self.join_clause[i] == '!=' or self.join_clause[i] =='=':
				continue
			elif self.join_clause[i] not in columns:
				index1=columns.index(self.join_clause[i-2])
				#print(datatypes[index1])
				if datatypes[index1] == 'int':
					if(self.join_clause[i].isdigit()):
						continue
					else:
						print("Incompatible Types")
						return False

				elif datatypes[index1] == 'numeric':
					if(self.join_clause[i].isdigit()):
						continue
					else:
						print("Incompatible Types")
						return False

				
				elif datatypes[index1] == 'date':
					try:
						datetime.datetime.strptime(self.join_clause[i], '%d-%m-%Y')
						continue	
					except ValueError:
						print("Wrong Date Format!")						
						return False
						
				elif datatypes[index1] == 'varchar':
					continue

		return True					

	def checkValidWhere(self):
		col=[]
		columns=[]

		datatype=[]
		dat=[]
		
		for i in range(0,len(self.tblname)):
			columns=meta.getAllColumns(self.tblname[i])
			datatypes=meta.getAllDatatypes(self.tblname[i])			
			columns=col+columns
			col=columns
			datatypes=dat+datatypes
			dat=datatypes

		print("columns",columns)
		print("cols",col)
		print(self.where_operation)		
		for i in range(0,len(self.where_operation)):
			print(self.where_operation[i])
			print(columns)
			if self.where_operation[i] == 'and' or self.where_operation[i] == 'or':
				continue
			elif self.where_operation[i] in columns:
				continue
			elif self.where_operation[i] == '<':
				continue
			elif self.where_operation[i] == '>':
				continue
			elif self.where_operation[i] == '!=':
				continue
			elif self.where_operation[i] == '=':
				continue
			
			elif self.where_operation[i] not in columns:
				print(self.where_operation[i])
				if self.where_operation[i-1] == '<' or self.where_operation[i-1] == '>' or self.where_operation[i-1] == '=' or self.where_operation[i-1]=='!=':
					if self.where_operation[i-2] in columns:
						index1=columns.index(self.where_operation[i-2])
					print(index1)
					if datatypes[index1] == 'int':
						if(self.where_operation[i].isdigit()):
							continue
						else:
							print("Incompatible Types")
							return False

					elif datatypes[index1] == 'numeric':
						if(self.where_operation[i].isdigit()):
							continue
						else:
							return False

				
					elif datatypes[index1] == 'date':
						try:
							datetime.datetime.strptime(self.where_operation[i], '%d-%m-%Y')
							continue	
						except ValueError:
							print("Wrong Date Format!")						
							return False
						
					elif datatypes[index1] == 'varchar':
						try:
							datetime.datetime.strptime(self.where_operation[i], '%d-%m-%Y')
							print("Date was given")
							return False							
								
						except ValueError:														
							continue
					else:											
						return False
				if i == 0 and self.where_operation[i] not in columns:
					print("Invalid Column 2")					
					return False
				else:
					
					print("hehe",i)
					
				''''
				else:
					print(self.where_operation[i-2])
					if type(self.where_operation[i-2])==str:
						print(self.where_operation[i],"is Invalid")
					else:					
						index1=columns.index(self.where_operation[i-2])
						#print(self.where_operation)
				#print(self.where_operation[i],self.where_operation[i-2])
					if datatypes[index1] == 'int':
						if(self.where_operation[i].isdigit()):
							continue
						else:
							print("Incompatible Types")
							return False

					elif datatypes[index1] == 'numeric':
						if(self.where_operation[i].isdigit()):
							continue
						else:
							return False

				
					elif datatypes[index1] == 'date':
						try:
							datetime.datetime.strptime(self.where_operation[i], '%d-%m-%Y')
							continue	
						except ValueError:
							print("Wrong Date Format!")						
							return False
						
					elif datatypes[index1] == 'varchar':
						try:
							datetime.datetime.strptime(self.where_operation[i], '%d-%m-%Y')
							print("Date was given")
							return False							
								
						except ValueError:														
							continue
				'''
		return True

	def getTblDelete(self):
		i=self.statementList.index('from')+1
		self.tblname.append(self.statementList[i])
		return self.tblname
		#print(self.tblname)		

	def getTblUpdate(self):
		i=self.statementList.index('set')-1
		self.tblname.append(self.statementList[i])
		print(self.tblname)		
		return self.tblname


	def getColumns(self):
		col=[]
		col1=[]
		data1=[]		
		self.columns=[]
		self.newValues=[]
		values=[]
		i=self.statementList.index('set')+1
		while(i<len(self.statementList)):
			if self.statementList[i] == "where":
				break
			else:
				col.append(self.statementList[i])
				i=i+1

		for i in range(0,len(col),3):
			self.columns.append(col[i])
		
		for i in range(2,len(col),3):
			values.append(col[i])		
		col1=meta.getAllColumns(self.tblname[0])
		data1=meta.getAllDatatypes(self.tblname[0])
		#print(col1,data1)

		for i in range(0,len(values)):
			ind=col1.index(self.columns[i])
			if data1[ind] == "int":
				self.newValues.append(int(values[i]))
			elif data1[ind] == "numeric":
				self.newValues.append(float(values[i]))
			else:
				self.newValues.append(str(values[i]))
		
				
		return self.columns,self.newValues

	def checkValidColumns(self):
		columns=[]
		col=[]	
		
		for i in range(0,len(self.tblname)):
			columns=meta.getAllColumns(self.tblname[i])
			columns=col+columns
			col=columns
			
		for i in range(0,len(self.columns)):
			if self.columns[i] not in columns:
				print(self.columns[i],"Invalid Column")
				return False

			return True			
	

	def select_tree(self):
		self.targetPrint=[];
		self.tblname=[];
		self.where_operation=[]
		self.join_clause=[]
		
		if self.operation == "select":
			
		#get the targetPrints
			self.targetPrint=self.getTargetPrint()		
			self.tblname=self.getTables()
			self.join_clause = self.getJoinClause()		
			self.where_operation = self.getWhere()		

			if(self.checkValidTargetPrint()):
				if(self.checkValidTables()):
					print("Valid Tables")
					if(len(self.join_clause)>0):
						
						if(self.checkValidJoin()):
							print("valid join")
							if(len(self.where_operation)>0):
								if(self.checkValidWhere()):
									print("Valid where 2")
									return True
								else:
									print("Invalid where")
									return False
							else:
								print("Join without where")
								return True
							
						else:
							return False
					if(len(self.where_operation)>0):
						if(self.checkValidWhere()):
							print("Valid Where 1")
							return True
						else:
							print("Invalid Where")
							return False
					else:
						print("Print table only")
						return True
				else:
					("Invalid Tables")
					return False
			else:
				print("Invalid Columns")
				return False
			return True

		elif self.operation == "delete":
			self.tblname=self.getTblDelete()
			self.where_operation = self.getWhere()

			if(self.checkValidTables()):			
				if len(self.where_operation) > 0:
					if(self.checkValidWhere()):
						return True
					else:
						return False
				else:
						return True
			else:
				return False

		elif self.operation == "update":
			print("update")
			self.tblname=self.getTblUpdate()
			self.columns,self.newValues = self.getColumns()
			self.where_operation = self.getWhere()
			print(self.columns,self.newValues)
			if(self.checkValidTables()):
				if(self.checkValidColumns()):
					if len(self.where_operation)>0:
						if(self.checkValidWhere()):
							return True
						else:
							return False
					else:
						return True
				else:
					return False
					
			else:
				return False
				
			#print(self.where_operation)

	def returnColumns(self):
		return self.columns

	def returnNewValues(self):
		return self.newValues			

	def returnTargetPrint(self):
		return self.targetPrint

	def returnTblname(self):
		return self.tblname

	def returnJoinClause(self):
		return self.join_clause

	def returnWhere(self):
		return self.where_operation


