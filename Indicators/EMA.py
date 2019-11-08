
class EMA:

	def __init__(self):
		pass

	def calculate(self, priceList, period):
		
		priceList = array(priceList)
		ema = []
		j = 1

		#CALCULATES SMA FIRST
		sma = sum(priceList[:period]) / period

		multiplier = 2 / float(1 + n)


		ema.append(sma)
		# CURRENT EMA = ((Price(Current) - EMA(Previous)) * Multiplier) + EMA(Previous)
		ema.append((s[j] - sma) * multiplier + sma)

		for i in s[n + 1:]:
			temp = ( (i - ema[j]) * multiplier) + ema[j]
			j++
			ema.append(temp)


		return ema