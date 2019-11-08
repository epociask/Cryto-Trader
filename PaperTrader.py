from priceTracker import PriceTracker as PT
import schedule
from SMADataHandler import *




class PaperTrader:



	def __init__(self, startingInvestment, coin, firstSma, secondSma):

		self.coinName = coin
		self.start = startingInvestment
		self.PRICE_TRACKER = PT(coin)
		self.percentageChange = 0.0
		self.isActive = True
		self.shouldCalculateStopLoss = True
		self.areSMAvalsProper = False
		self.buyCrossover = False
		self.priceGainLoss = 0.0
		self.SMAcrossover = False
		self.stopLosssCalcluated = False
		self.previousPrice = self.PRICE_TRACKER.getPriceFloat()
		self.currentPrice = self.PRICE_TRACKER.getPriceFloat()
		self.crossoverHandler = SMADataHandler(firstSma, secondSma, coin)
		self.SMAS = self.crossoverHandler.getSMA_data()
		self.firstSma = 0
		self.secondSma = 0

	def buy():

		#BUY WHEN WE HAVE CORRECT SMA VALUES STORED AND A CROSS-OVER IS DETECTED 
		print("BUYING")
		self.buyPrice = PT.getPriceFloat()
		self.assetHeld = self.start/self.buyPrice
		self.stopLoss = self.calcStopLoss(self.buyPrice, self.PRICE_TRACKER.getPriceFloat())
		self.stopLosssCalcluated = True


	#Closes connection to the retrieval query classes
	#Determines sell price
	def sell(self):
		self.sellPrice = self.PRICE_TRACKER.getPriceFloat()
		self.PRICE_TRACKER.closeConnection()
		self.crossoverHandler.closeConnection()

	#determines sell... ONLY SELL IF price goes lower than stop loss
	def determineToSell(self):
		if self.stopLosssCalcluated == True:
			if self.currentPrice <= self.stopLoss:
				self.sell()
				self.isActive = False



	def determineToBuy(self):

		if self.areSMAvalsProper == True and self.SMAcrossover == True:
			self.buy()

	#Calculates 1% loss priceValue of currentPrice 
	def calcStopLoss(self, buyIn, currentPrice):
		return currentPrice*.99

	def updateData(self):


		self.previousPrice = self.currentPrice

		self.currentPrice = self.PRICE_TRACKER.getPriceFloat()

		if self.shouldCalculateStopLoss == True:
			self.stopLoss = self.calcStopLoss(self.currentPrice, self.PRICE_TRACKER.getPriceFloat())

		if (self.areSMAvalsProper == True) and (self.firstSma > self.secondSma):
			self.SMAcrossover == True
		#IF price starts going down, then we will stop calculating stop loss
		if self.previousPrice >= self.currentPrice:
			self.shouldCalculateStopLoss = False
	

		self.SMAS = self.crossoverHandler.getSMA_data()



		if self.SMAS[0] != 0:
			self.firstSma = self.SMAS[0]


		if self.SMAS[1] != 0:
			self.secondSma = self.SMAS[1]


		if self.firstSma != 0 and self.secondSma != 0:
			self.areSMAvalsProper = True

		print(self.coinName, self.currentPrice)

		if self.areSMAvalsProper == True:
			print(self.firstSma, self.secondSma)





testTrade = PaperTrader(3000 , "bitcoin", "1", "5")





