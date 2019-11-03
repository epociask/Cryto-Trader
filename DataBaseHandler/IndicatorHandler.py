#!/usr/bin/python
import psycopg2
from config import config
from datetime import datetime
import time, sys, json, datetime
from CoinCap import CoinCap
import keyboard
from Indicators import *


TABLE_NAME = "bitcoin_indicator_data"

class IndicatorDataWriter:

  def __init__(self, coin):
    self.coin = coin
    self.TABLE_NAME = "{}_indicator_data".format(self.coin)

  # Returns query string to insert data into db


  def runDataInsertions(self, cursor):
    try:
      		
      print("Time: {} Price: {} 24 hr Volume: {} Market Cap: {}".format(datetime.datetime.now(), price, dayVolume, marketCap))
      insertQuery = self.generateQuery(price, marketCap, dayVolume)
      cursor.execute(insertQuery)

    except(Exception) as error:
      print("ERROR INSERTING DATA: ", error)

  # Connects to the db via psycopg2 and inserts data
  def connect(self):
    """ Connect to PGSQL server """
    conn = None

    try:
      params = config()
      print("Connecting to postgres database...")
      conn = psycopg2.connect(user = "postgres",
                                  password = "1Derekdad1",
                                  host = "localhost",
                                  port = "5433",
                                  database = "coindata")


      # create a cursor
      cur = conn.cursor()

      # Generate and execute insertion query
      print("Starting data collection... Press q to quit")
      while(True):
        if(keyboard.is_pressed('q')):
          print("Stopping data collection.")
          break
        self.runDataInsertions(cur)
        conn.commit() # Commits changes to db

      cur.close() # Closes communication with db
    except(Exception, psycopg2.DatabaseError) as error:
      print("ERROR: ", error)
    finally:
      if conn is not None:
        conn.close()
        print('Database connection closed.')

