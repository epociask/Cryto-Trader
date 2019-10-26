

class MovingAverageCalculator:

	def __init__(self, averagelist, timePeriod):
		self.averagelist = averagelist
		self.timePeriod = timePeriod
		self.movingAverage = calculate(self)




	def calculate(self):
		sumf = 0
		for i in self.averagelist:
			sumf += self.averagelist[i]

		sumf = sumf / len(self.averagelist)

		return sumf / timePeriod

