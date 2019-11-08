import psycopg2
from config import config
from datetime import datetime
import time, sys, json, datetime
from Time import *
from SMA import *

class IndicatorDataWriter:

  def __init__(self, coin):
    self.coin = coin
    self.INDICATOR_TABLE_NAME = "{}_indicators".format(self.coin)
    self.PRICE_TABLE_NAME = "{}_price_data".format(self.coin)
    self.time = Time()
    self.sma = SMA()
    print("Connecting to postgres database...")

    self.CONN = psycopg2.connect(**config())

  #SELECTS TIME_STAMP & PRICE DATA FROM COIN_PRICE_DATA
  def SelectQuery(self, timeLength):

    self.timeStep = self.time.calculateTime(timeLength)
    self.timeRef = self.time.calculateRef(timeLength)

    return "SELECT time_stamp, price FROM {} ORDER BY time_stamp DESC LIMIT {};".format(self.PRICE_TABLE_NAME, self.timeStep)


  def createTableQuery(self):
    return "CREATE TABLE {} (time_stamp timestamp without time zone DEFAULT CURRENT_TIMESTAMP PRIMARY KEY NOT NULL, sma_1 numeric , sma_5 numeric , sma_10 numeric , sma_30 numeric , sma_60 numeric , sma_180 numeric , sma_360 numeric , sma_720 numeric , sma_1440 numeric );".format(self.INDICATOR_TABLE_NAME)
  #INSERTS CALCULATED SMA VALUE INTO INDICATOR TABLE
  def insertionQuery(self, data):

      return "INSERT INTO {} (sma_{}) VALUES ({});".format(self.INDICATOR_TABLE_NAME, self.timeRef, data)

  def runDataCollection(self, cursor, timeLength):
    try:
      
      Query = self.SelectQuery(timeLength)
      cursor.execute(Query)
      x = cursor.fetchall()
      count = 0
      for i in x:
        i = str(i)
        x[count] = float((i[i.find("Decimal")+9 : len(i)-3]))
        count+=1
      print(x)
      cursor.execute(self.insertionQuery(self.sma.calculateSMA(x)))
      return None
    except(Exception) as error:
      print("ERROR COLLECTING/INSERTING DATA: ", error)
      return error

 # Connects to the db via psycopg2 and inserts data
  def connect(self, timeLength):
    """ Connect to PGSQL server """
        # create a cursor
    cur = self.CONN.cursor()    

      # Generate and execute insertion quer
    err = self.runDataCollection(cur, timeLength)
    if err != None:
      curr = conn.cursor()
      curr.execute(self.createTableQuery())
      self.CONN.commit()
      self.connect()

    self.CONN.commit() # Commits changes to db
    cur.close() # Closes communication with db
    print('Cursor connection closed.')

  def closeConnection(self):
    self.CONN.close()