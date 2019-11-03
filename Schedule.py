from PriceDataHandler import *
from IndicatorDataWriter import *
import schedule
import time

class Schedule:

	def __init__(self, coinName):
		self.API_WRITER = PriceDataHandler(coinName)
		self.DISTRIBUTOR = IndicatorDataWriter(coinName)


	
	def start(self):

		schedule.every(5).seconds.do(self.API_WRITER.connect())
		schedule.every(1).minute.do(self.DISTRIBUTOR.connect("one-minute"))
		schedule.every(5).minute.do(self.DISTRIBUTOR.connect("five-minute"))
		schedule.every(10).minute.do(self.DISTRIBUTOR.connect("ten-minute"))
		schedule.every(30).minute.do(self.DISTRIBUTOR.connect("thirty-minute"))

		

		while 1:
			schedule.run_pending()
			time.sleep(1)
