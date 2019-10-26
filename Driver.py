#from PricePlotter import *
from Schedule import *
from threading import Thread



#plotter = PricePlotter()
test1 = Schedule()


test1.start()
#test2.start()
#updater.update()

proc1 = Thread(target = test1.start())
proc2 = Thread(target = test2.start())

proc2.start()
proc1.start()