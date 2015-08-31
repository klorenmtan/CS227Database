from Data import *
import copy
from Metadata import *
class FileReader:
	def __init__(self,filename):
		self.filename   = filename
		self.dictValues = dict()
		self.keyList 	= []
		self.clean_data = {}
		self.database = []
		data1=[]
	
	def fileRead(self,data):
		
		fileR = open(self.filename+".csv","r")
		for line in fileR:
			line = line[:-1]
			data1 =line.split(",")
			data.append(list(data1))
		fileR.close()
		self.data = data		
		
		
	def hashData(self):
		
		dt = Data(self.data,self.filename)
		self.clean_data=dt.getDataHash()
		self.database.append(self.clean_data)		
		return self.database

	def printData(self,tblname):
		md = Metadata()
		self.no_columns = md.no_getColumns(tblname)
		print((self.database))		
		#print (no_columns, type(no_columns))
		#for i in range(0,len(self.database)):
		#	print()
			

