class PaperTraderDriver:

	#Compares param1 to param2 as crossover indication to buy withing PaperTrader class
	def __init__(self, tradingStrategy, param1, param2):

	



	def trade(self):

		schedule.every(1).seconds.do(testTrade.updateData)
		schedule.every(1).seconds.do(testTrade.determineToBuy)	
		schedule.every(1).seconds.do(testTrade.determineToSell)		

		

		while 1:
			schedule.run_pending()
			time.sleep(1)
