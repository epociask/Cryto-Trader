#Property of TrendSellers LLC 
#@author Ethen Pociask


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import os



class PricePlotter:



	def __init__(self, name, variable):

		self.name = name
		self.variable = variable

		style.use('fivethirtyeight')

		fig = plt.figure()



		ax1 = fig.add_subplot(1,1,1)
		ani = animation.FuncAnimation(fig, self.animate, interval = 1000, repeat = True)

		plt.ylabel("Price $")
		plt.xlabel("Time")
		plt.title(name + "Live Price Tracking")
		plt.show()

	def animate(self, i):

		os.chdir('..')

		file = open('DataBase/' + self.name + "/" + self.name + self.variable + ".txt", "r").read()

	
		lines = file.split("\n")

		xs = []
		ys = []

	
		for line in lines:
			x = line[0 : line.find(",")]
			x = x[5 : len(x)]
			y = line[line.find(",") : len(line)]
			y = y.replace(",", "")
	

			try:
				ys.append(float(y))
				xs.append(x)


			except ValueError:	
				break
		
		ax1.clear()	#xs = 
	#ys = ys[ys.find(",") : ys.find(",")+7]
		ax1.plot(xs, ys)

		



