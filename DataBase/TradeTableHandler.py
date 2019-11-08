import psycopg2
from config import config

#Writes trade information of buy/sell when completed 
class TradeTableHandler:


	def__init__(self, coin):

		self.coinName = coin
		self.CONN = psycopg2.connect(config())



	def insertToTradeTable(self, coinName, buyIn, profitLoss, didProfit, strategy):

		return "INSERT INTO (time_stamp, COIN, BUY_IN,  PROFIT_LOSS, DID_PROFIT, Strategy_Used, TRADE_TABLE) VALUES ({}, {}, {}, {}, {});"



	def writeToTable(self, coinName, buyIn, profitLoss, didProfit, strategy):
		CUR = self.CONN.cursor()
		CUR.execeute(insertToTradeTable())
		CUR.close()
		self.CONN.close()
