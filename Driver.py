from Schedule import *
import multiprocessing as mp



def main():

	pool = mp.Pool(mp.cpu_count())


	pool.map(Schedule, ["ethereum", "bitcoin", "ripple", "litecoin"])


if __name__ == "__main__":
	main()
