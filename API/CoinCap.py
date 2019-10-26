import requests 
#@Author Ethen Pociask
#DATA API REQUEST CLASS
class CoinCap:
	
	#TAKES COIN NAME AS PARAM 
	def __init__(self, asset):

		self.asset = asset
		self.APIURL = "http://api.coincap.io/v2/assets/" + self.asset



	def getData(self):


		PARAMS = {'limit': 1}
		try:
			r = requests.get(url = self.APIURL, params = PARAMS)

		except:
			self.getData()

		l = []

		dic = {}
		data = str(r.json())
		l = data.split("{")
		l = l[2].split(",")

		for val in l:

			for letter in val:
				val = val.replace(" ", "")
			dic[val[1:val.index(':')-1]] = val[val.index(':')+2 : len(val)-1]
		#crytoData = parser.toCrypto()
		return str(dic)


