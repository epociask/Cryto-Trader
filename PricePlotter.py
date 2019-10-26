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



		self.ax1 = fig.add_subplot(1,1,1)
		self.ani = animation.FuncAnimation(fig, self.animate, interval = 1000, repeat = True)

		plt.ylabel("Price $")
		plt.xlabel("Time")
		plt.title(name + " Live Price Tracking")
		plt.show()

	def animate(self, i):



		file1 = open('DataBase/' + self.name + "/" + self.name + self.variable + ".txt", "r").read()
		base = file1.split("\n")

		file2 = open('DataBase/' + self.name + "/SMA/five-minute.txt", "r").read()
		base2 = file2.split("\n")
		otherLines = base2[len(base2) - 100 : len(base2)]
		lines = base[ len(base) - 100: len(base)]
		xs = []
		ys = []
		zs = []

		for line in otherLines:
			z = line[line.find(",")+1 : len(line)] 
			print(z)
			try: 
				zs.append(float(z))

			except ValueError:
				break

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
		#print(len(xs), len(ys), len(zs))
		xs.pop()
		ys.pop()
		self.ax1.clear()
	#ys = ys[ys.find(",") : ys.find(",")+7]
		self.ax1.plot(xs, ys, '-g')
		self.ax1.plot(xs, zs, '-y')


