import psycopg2
from config import config
from datetime import datetime
import time, sys, json, datetime
from CoinCap import CoinCap



class PriceDataHandler:

  def __init__(self, coin):
    self.coin = coin
    self.TABLE_NAME = "{}_price_data".format(coin)
    self.CONN = psycopg2.connect(**config())

  def createTableQuery(self):
    print("Creating table query")
    return "CREATE TABLE {} (day_volume numeric, price numeric, market_cap numeric, time_stamp timestamp without time zone DEFAULT CURRENT_TIMESTAMP);".format(self.TABLE_NAME)
  # Returns query string to insert data into db
  def generateQuery(self, price, marketCap, dayVolume):
    columns = "(day_volume, price, market_cap)"
    values = "({}, {}, {})".format(dayVolume, price, marketCap)
    return "INSERT INTO " + self.TABLE_NAME + " " + columns + " VALUES " + values + ";"

  ## Parses data from API and returns price, day volume, and market cap
  def parseCoinData(self):
    coinCap = CoinCap(self.coin)
    data = coinCap.getData()
    price = data.get('data').get('priceUsd')
    dayVolume = data.get('data').get('volumeUsd24Hr')
    marketCap = data.get('data').get('marketCapUsd')

    return price, dayVolume, marketCap

  def runDataInsertions(self, cursor):
    try:
      price, dayVolume, marketCap = self.parseCoinData()
      print("Time: {} Price: {} 24 hr Volume: {} Market Cap: {}".format(datetime.datetime.now(), price, dayVolume, marketCap))
      insertQuery = self.generateQuery(price, marketCap, dayVolume)
      cursor.execute(insertQuery)
      return None
    except(Exception) as error:
      print("ERROR INSERTING DATA: ", error)
      return error


  # Connects to the db via psycopg2 and inserts data
  def connect(self):
    """ Connect to PGSQL server """
      # create a cursor
    cur = self.CONN.cursor()
      # Generate and execute insertion query
    err = self.runDataInsertions(cur)
    self.CONN.commit() # Commits changes to db
    cur.close() # Closes communication with db
    if err != None:
      cur = conn.cursor()
      cur.execute(self.createTableQuery())
      self.CONN.commit()
      self.connect()
    self.CONN.commit() # Commits changes to db
    cur.close()


  def closeConnection(self):
    self.CONN.close()
    print('Database connection closed.')


