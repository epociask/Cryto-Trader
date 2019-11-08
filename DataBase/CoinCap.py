import requests
#@Author Ethen Pociask
#DATA API REQUEST CLASS
class CoinCap:

	#TAKES COIN NAME AS PARAM
	def __init__(self, asset):

		self.asset = asset
		self.APIURL = "http://api.coincap.io/v2/assets/" + self.asset

	# Returns json data from api
	def getData(self):


		PARAMS = {'limit': 1}
		try:
			r = requests.get(url = self.APIURL, params = PARAMS)

		except Exception:
			self.getData()
		data = r.json()

		return data



