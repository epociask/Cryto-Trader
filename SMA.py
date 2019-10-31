#Property of TrendSellers LLC
#@author Ethen Pociask

class AverageCalculator:

	def __init__(self):
		pass

	def calculateSMA(self,  priceSet):
		priceTotal = 0

		for price in priceSet:
			total = total + float(price)

		return priceTotal/len(priceSet)
