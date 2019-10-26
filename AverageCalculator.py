#Property of TrendSellers LLC 
#@author Ethen Pociask

class AverageCalculator:

	def __init__(self, priceSet):
		self.priceSet = priceSet
		print(priceSet)

	#finds Simple Moving Average for given timeFrame passed in init
	#assigns equal weighting to all values
	def calculateSMA(self):
		priceTotal = self.sum(self.priceSet)


		return priceTotal/len(self.priceSet)


	def sum(self, priceSet):
		priceTotal = 0
		for price in priceSet:
			price = float(price)
			priceTotal += price
		return priceTotal

	def calculateEMA(self, length):

		multiplier = (2 / (length + 1))

		firstEMA = self.sum(self.priceSet)
		
		
