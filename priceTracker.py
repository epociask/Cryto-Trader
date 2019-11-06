import psycopg2
from config import config
import time, sys, json, datetime




class PriceTracker:


	def __init__(self, coinName):
		self.coinName = coinName
		self.CONN = psycopg2.connect(**config())




	def getPriceFromQuery(self):
		return "SELECT time_stamp, price FROM {}_price_data ORDER BY time_stamp DESC LIMIT 1;".format(self.coinName)



	def parseString(self, string):
		return string[string.find("Decimal") + 9: len(string) - 4]



	def getPriceFloat(self):


		self.CURS = self.CONN.cursor()

		self.CURS.execute(self.getPriceFromQuery())

		return float(self.parseString(str(self.CURS.fetchall())))

	def closeConnection(self):

		self.CURS.close()
		self.CONN.close()




