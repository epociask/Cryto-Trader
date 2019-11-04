#Property of TrendSellers LLC 
#@author Ethen Pociask

class SMA:

	def __init__(self):
		pass

	def calculateSMA(self,  priceSet):
		priceTotal = 0

		for price in priceSet:
			priceTotal = priceTotal + float(price)



		return priceTotal/len(priceSet)



	
