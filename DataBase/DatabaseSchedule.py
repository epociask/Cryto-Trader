import schedule
import time

class DatabaseSchedule:

	def __init__(self, coinName):
		self.coinName = coinName
		self.price_data_handler = PriceDataHandler(self.coinName)
		self.indicator_data_handler = IndicatorDataWriter(self. coinName)
		


	def start(self):
		schedule.every(5).seconds.do(self.price_data_hander.connect)
		schedule.every(1).minutes.do(self.indicator_data_handler.connect, ("one-minute"))
		schedule.every(5).minutes.do(self.indicator_data_handler.connect,("five-minute"))
		schedule.every(10).minutes.do(self.indicator_data_handler.connect,("ten-minute"))
		schedule.every(30).minutes.do(self.indicator_data_handler.connect,("thirty-minute"))		

		

		while 1:
			schedule.run_pending()
			time.sleep(1)
