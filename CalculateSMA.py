#@author Ethen Pociask

from AverageCalculator import *
from Time import *
class CalculateSMA:

	def __init__(self):
		pass
		
		
	def calculateSMA(self, currencyName, timePeriod):

		time = Time()		
		name = currencyName

		file = open("DataBase/"+name+"/"+name+"priceUsd.txt").read()
		Set = file.split("\n")

		step = time.calculateTime(timePeriod)

		dataSet = Set[len(Set)-step : len(Set)]

		justPrice = dataSet

	
		timeStamp = justPrice[len(justPrice)-1]
		for data in justPrice:
			justPrice[justPrice.index(data)] = data[data.find(",")+1 : len(data)-1]
		

		calc = AverageCalculator(justPrice)
		SMA = calc.calculateSMA()
		f = open('DataBase/'+name+"/SMA/"+timePeriod+".txt", "a")

		f.write(timeStamp[0 : 15] + ", " +str(SMA) + "\n")

		f.close()


	

