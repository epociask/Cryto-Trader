from FileWriter import *
import schedule
import time
from CalculateSMA import *

class Schedule:

	def __init__(self):
		self.writer = FileWriter()
		self.calc = CalculateSMA()

	
	def start(self):

		schedule.every(1).seconds.do(self.writer.writeUpdate , 'bitcoin') 
		schedule.every(1).seconds.do(self.writer.writeUpdate , 'ethereum') 
		schedule.every(1).minutes.do(self.calc.calculateSMA , 'ethereum', 'one-minute')
		schedule.every(5).minutes.do(self.calc.calculateSMA , 'ethereum', 'five-minute')
		schedule.every(10).minutes.do(self.calc.calculateSMA , 'ethereum', 'ten-minute')
		schedule.every(1).minutes.do(self.calc.calculateSMA , 'bitcoin', 'one-minute')
		schedule.every(5).minutes.do(self.calc.calculateSMA , 'bitcoin', 'five-minute')
		schedule.every(10).minutes.do(self.calc.calculateSMA , 'bitcoin', 'ten-minute')

		while 1:
			schedule.run_pending()
			time.sleep(1)
