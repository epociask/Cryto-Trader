class Time:

	def __init__(self):
			pass

	def calculateTime(self, timePeriod):

		step, ref = 0
		if timePeriod == "one-minute":
			step = 12
			ref = 1

		elif timePeriod == "five-minute":
			step = 60
			ref = 5
		elif timePeriod == "ten-minute":
			step = 120
			ref = 10
		elif timePeriod == "thirty-minute":
			step = 360
			ref = 30
		elif timePeriod == "one-hour":
			step = 720
			ref = 60

		return step, ref

	