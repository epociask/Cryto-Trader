import psycopg2
from config import config
import time, sys, json, datetime



class SMADataHandler:

	def __init__(self, firstSMA, secondSMA, coinName):
		self.firstSMA = firstSMA
		self.secondSMA = secondSMA
		self.coinName = coinName
		self.CONN = psycopg2.connect(**config())
		print("ESTABLISHING CONNECTION TO DATABASE")



	def getRetrievalQuery(self, smaVal):

		return "SELECT time_stamp_1 ,sma_{} FROM {}_indicators ORDER BY time_stamp_1 DESC LIMIT 1;".format(smaVal, self.coinName)


	def getSMA_Data(self, smaVal, curs):		
		curs.execute(self.getRetrievalQuery(smaVal))
		return curs.fetchall()

	def getSMA_data(self):
		curs = self.CONN.cursor()
		x = []
		x.append(float(self.parseString(str(self.getSMA_Data(self.firstSMA, curs)))))
		x.append(float(self.parseString(str(self.getSMA_Data(self.secondSMA, curs)))))
		curs.close()
		return x

	def parseString(self, string):

		if "None" in string:
			return "0"
		return string[string.find("Decimal") + 9: len(string) - 4]

	def closeConnection(self):
		print("CLOSING CONNECTION TO DATABASE")
		self.CONN.close()





