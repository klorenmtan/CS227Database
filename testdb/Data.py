from Metadata import *
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
		#print (self.clean_data)
		return self.clean_data

	def PrintDataALL(tblname, database):
		count=0;
		for i in range(0,len(tblname)):
			column=md.getAllColumns(tblname[i])
			for j in range(0,len(database[tblname[i]])):				
				for k in range(0,len(column)):			
					print("",database[tblname[i]][str(j+1)][column[k]],"\t",end='')
					
				print()
				count=count+1					

		print(count,"rows returned") 
				
	def PrintColumn(tblname,targetPrint,database):
		num=0
		return_select=[]
		datahash=list()	
		count=0
		for i in range(0,len(tblname)):
			for j in range(0,len(database[tblname[i]])):
				for k in range(0,len(targetPrint)):
					if targetPrint[k] in database[tblname[i]][str(j+1)] and num==0:
					   
					   datahash.append(database[tblname[i]][str(j+1)][targetPrint[k]])
					elif targetPrint[k] in database[tblname[i]][str(j+1)] and num!=0:
						
						datahash.append(database[tblname[i]][str(j+1)][targetPrint[k]])
						#print(database[tblname[i]][str(j+1)][targetPrint[k]])
					else:
						continue
				return_select.append(datahash)
				datahash=[]				
			num=1
		print(return_select)
		print(count,"rows returned")
'''		print(targetPrint)
		for i in range(0,len(tblname)):
			#column=md.getAllColumns(tblname[i])
			for j in range(0,len(database[tblname[i]])):				
				for k in range(0,len(targetPrint)):
					if targetPrint[k] in database[tblname[i]][str(j+1)]:			
						print("",database[tblname[i]][str(j+1)][targetPrint[k]],"\t",end='')
						datahash[targetPrint[k]]=database[tblname[i]][str(j+1)][targetPrint[k]]

					else:
						continue
				
				datahash={}
				#print()
				count=count+1					
'''		
		


