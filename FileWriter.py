from datetime import datetime
from API.CoinCap import CoinCap
import os 

class FileWriter:

	def __init__(self): 
		self.time = "";


	def writeUpdate(self, name):
		#JSON Data is parsed as dictionary
		API = CoinCap(str(name))
		data = API.getData()

		file =  open('DataBase/'+name+'/' + name + '.txt' , "w")
		file.write(data+"\n")
		
		file.close()

		#x = str(data['timestamp'])
		#y = str(data['priceUsd'])
		#priceFile.write(x +"," +y +"\n")
		#priceFile.close()



