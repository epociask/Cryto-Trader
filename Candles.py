class Candle:


	def __init__(self, coinName):

			self.coinName = coinName


	def generateCandle(self, timeLength):
		readFile = open('DataBase/' + coinName + '/' + 'priceUsd').read()

		mini = 100000000000000
		maxi = 0 
		for line in readFile:
			price = line[0 : line.find(",")]
			
			if price > maxi:
				maxi = price 

			if price < mini:
				mini = price

		self.high = maxi
		self.low = mini