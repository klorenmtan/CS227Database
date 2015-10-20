from Metadata import *
from prettytable import *
import itertools

class Data:

	def __init__(self,tbldata,tblname):
		global md
		md=Metadata()		
		self.database={}
		self.tbldata = tbldata
		self.tblname = tblname
		self.clean_data = {}
		self.getPrimary()
		self.addToHash()


	def getPrimary(self):
		self.primary_keys=[]
		for i in range (0,len(self.tbldata)):
			self.primary_keys.append((self.tbldata[i][0]))
		return self.primary_keys
		

	def addToHash(self):
		items={}		
		items1={}
		items2={}
		columns=md.getAllColumns(self.tblname)
		datatype =md.getAllDatatypes(self.tblname)

		#convertion
		for i in range(0,len(datatype)):			
			for j in range(0,len(self.tbldata)):	
				
				if datatype[i] == 'numeric':
				#	print(self.tbldata[j][i])
				#	print("NUMERIC")
					self.tbldata[j][i]=float(self.tbldata[j][i])
					
				if datatype[i] == 'int':
				#	print(self.tbldata[j][i])
				#	print("INT")
					self.tbldata[j][i]=int(self.tbldata[j][i])
					
				else:			
				#	print(self.tbldata[j][i])
				#	print("STRING")
					self.tbldata[j][i]=(self.tbldata[j][i])
					
											
		for i in range(0,len(self.tbldata)):
			for j in range(0,len(columns)):
				items={columns[j]:self.tbldata[i][j]}
				items1.update(items)
			self.clean_data[self.primary_keys[i]]=items1			
			items1={}
			items={}
							
				
	def getDataHash(self):
		return self.clean_data

	def printData(datahash,tblname,targetPrint):
		header=[]
		row = PrettyTable()
		if len(datahash)==0:
			print("Empty Set")
		else:
			if len(targetPrint) == 1 and targetPrint[0] == "*":
				for j in range(0,len(tblname)):
					column =md.getAllColumns(tblname[j])
					header.extend(column)
				row.field_names = header
	
				#for i in range(0,len(datahash)):
				#	row.add_row(datahash[i])
				print(row)
				for i in range(0,len(datahash)):
					for j in range(0,len(datahash[i])):
						print(datahash[i][j]," ",end='')
					print()
			else:
				row.field_names=targetPrint
				print(row)
				for i in range(0,len(datahash)):
					for j in range(0,len(datahash[i])):
						print(datahash[i][j]," ",end='')
					print()			
				
		
	
	def printDataWhere(datahash,tblname,targetPrint,columns):
		header=[]
		row = PrettyTable()
		
		if len(datahash)==0:
			print("Empty Set")
		else:
			if len(targetPrint) == 1 and targetPrint[0] == "*":
				for j in range(0,len(tblname)):
					column =md.getAllColumns(tblname[j])
					header.extend(column)
				row.field_names = header

				print(row)
				for i in range(0,len(datahash)):
					for j in range(0,len(datahash[i])):
						print(datahash[i][j]," ",end='')
					print()


			else:
				#print(datahash)
				data=[]
				column=[]
				col = []
				fdata=[]
				for j in range(0,len(tblname)):
					column =md.getAllColumns(tblname[j])
					column = col + column
					col = column
					
				for i in range(0,len(datahash)):
					for j in range(0,len(targetPrint)):
						ind = column.index(targetPrint[j])
						data.append(datahash[i][ind])
					fdata.append(data)
					data=[]	
				
				row.field_names=targetPrint
				print(row)
				for i in range(0,len(datahash)):
					for j in range(0,len(datahash[i])):
						print(datahash[i][j]," ",end='')
					print()
			
				
	def crossProduct(list1, list2):
		list4=[]		
		list3=list1
		for i in range(0,len(list1)):
			for j in range(0,len(list2)):
				list4.append(list3[i]+list2[j])				
		return list4

	def PrintDataALL(tblname, database):
				
		return_data=[]
		datahash=[]		
		count=0;
		cross_data=[]
		k=0
		for j in range(0,len(tblname)):
			column=md.getAllColumns(tblname[j])	
			datahash=Data.getRows(tblname[j],column,database)
			return_data.append(datahash)

		#print(return_data)
		targetPrint=[]
		a=[]
		a=return_data[0]		
		j=0
		if len(tblname) > 1:
			for i in range(1,len(return_data)):			
				a=Data.crossProduct(a,return_data[i])			
			return a			
		else:
			return return_data[0]	
		
	def getRows(tblname,column_name,database):
		return_data=[]
		datahash=[]
		data = []
		counter=0

		for j in range(0,len(list(database[tblname].keys()))):
			for i in range(0,len(list(column_name))):
				if column_name[i] in database[tblname][(list(database[tblname].keys()))[j]]:
					data.append(database[tblname][(list(database[tblname].keys()))[j]][column_name[i]])						
			datahash.append(data)
			data=[]
		return datahash

	
		
	def PrintColumn(tblname,targetPrint,database):
		length=0
		count=0
		
		return_select=[]
		return_data = []
		datahash=list()
		
		for i in range(0,len(tblname)):		
			datahash=Data.getRows(tblname[i],targetPrint,database)
			return_data.append(datahash)
		
		
		a=[]
		a=return_data[0]		
		if len(tblname) > 1:
			for i in range(1,len(return_data)):			
				a=Data.crossProduct(a,return_data[i])			
			return a			
		else:
			return return_data[0]
		

	


