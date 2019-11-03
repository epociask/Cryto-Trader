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

  #SELECTS TIME_STAMP & PRICE DATA FROM COIN_PRICE_DATA
  def SelectQuery(self, timeLength):

    self.timeStep = self.time.calculateTime(timeLength)
    self.timeRef = self.time.calculateRef(timeLength)

    return "SELECT time_stamp, price FROM {} ORDER BY time_stamp DESC LIMIT {};".format(self.PRICE_TABLE_NAME, self.timeStep)


  #INSERTS CALCULATED SMA VALUE INTO INDICATOR TABLE
  def insertionQuery(self, data):

      return "INSERT INTO {} (time_stamp_{},sma_{}) VALUES ({} ,{});".format(self.INDICATOR_TABLE_NAME, self.timeRef, self.timeRef, datetime.datetime.now().timestamp(), data)

  def runDataCollection(self, cursor):
    try:
      
      Query = self.SelectQuery("one-minute")
      cursor.execute(Query)
      x = cursor.fetchall()
      count = 0
      for i in x:
        i = str(i)
        x[count] = float((i[i.find("Decimal")+9 : len(i)-3]))
        count+=1
      print(x)
      cursor.execute(self.insertionQuery(self.sma.calculateSMA(x)))
    except(Exception) as error:
      print("ERROR COLLECTING/INSERTING DATA: ", error)

 # Connects to the db via psycopg2 and inserts data
  def connect(self):
    """ Connect to PGSQL server """
    conn = None

    try:
      params = config()
      print("Connecting to postgres database...")
      conn = psycopg2.connect(user = "postgres",
                                  password = """"""",
                                  host = "localhost",
                                  port = "5433",
                                  database = "coindata")
      # create a cursor
      cur = conn.cursor()

      # Generate and execute insertion quer
      self.runDataCollection(cur)
      conn.commit() # Commits changes to db
      cur.close() # Closes communication with db
    except(Exception, psycopg2.DatabaseError) as error:
      print("ERROR: ", error)
    finally:
      if conn is not None:
        conn.close()
        print('Database connection closed.')

IndicatorDataWriter('bitcoin').connect()
