from PriceDataHandler import *
from IndicatorDataWriter import *
import schedule
import time

class Schedule:

	def __init__(self, coinName):
		self.coinName = coinName
		schedule.every(5).seconds.do(PriceDataHandler(self.coinName).connect)
		schedule.every(1).minutes.do(IndicatorDataWriter(self.coinName, "one-minute").connect)
		schedule.every(5).minutes.do(IndicatorDataWriter(self.coinName, "five-minute").connect)
		schedule.every(10).minutes.do(IndicatorDataWriter(self.coinName, "ten-minute").connect)
		schedule.every(30).minutes.do(IndicatorDataWriter(self.coinName, "thirty-minute").connect)



		while 1:
			schedule.run_pending()
			time.sleep(1)
