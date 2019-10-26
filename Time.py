class Time:

	def __init__(self):
			pass

	def calculateTime(self, timePeriod):

		step = 0
		if timePeriod == "one-minute":
			step = 12

		elif timePeriod == "five-minute":
			step = 60

		elif timePeriod == "ten-minute":
			step = 120

		elif timePeriod == "thirty-minute":
			step = 360

		elif timePeriod == "one-hour":
			step = 720


		return step