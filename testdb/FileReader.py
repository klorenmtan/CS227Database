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
		self.data1=[]
	
	def fileRead(self):
		data2 = []
		fileR = open(self.filename+".csv","r")
		for line in fileR:
			line = line[:-1]
			self.data1 =line.split(",")
			data2.append(list(self.data1))
		fileR.close()
		self.data = data2		
		
				
		
	def hashData(self):
		
		dt = Data(self.data,self.filename)
		self.clean_data=dt.getDataHash()
		print (self.clean_data)
		return self.clean_data

	def printData(self,tblname):
		md = Metadata()
		self.no_columns = md.no_getColumns(tblname)
		print((self.database))		
			

