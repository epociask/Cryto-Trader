# Crypto Trader

### Setting up the local database:
1. Make sure postgresql is installed
2. Start the postgres local server via `pg_ctl -D /usr/local/var/postgres start` on mac
3. Start the postgres shell: `psql -U postgres`
4. Create the database. Looks like this for now:

###Setting up connection to the database
1. 
### Generic Price Data Table DLL
```sql
CREATE TABLE bitcoin_price_data (
    day_volume numeric,
    price numeric,
    market_cap numeric,
    time_stamp timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
```

2.
### Generic Indicator Data Table DLL
### MADE ALL VALUES NUMERIC AS TIME_STAMP WILL VARY ACCORDING TO EACH VALUE
```sql
CREATE TABLE bitcoin_indicators (
	time_stamp_1 numeric,
    sma_1 numeric,
    time_stamp_5 numeric,
    sma_5 numeric,
    time_stamp_10 numeric,
    sma_10 numeric,
    time_stamp_30 numeric,
    sma_30 numeric,
    time_stamp_60 numeric,
    sma_60 numeric,
    time_stamp_180 numeric,
 	sma_180 numeric,
	time_stamp_360 numeric,
	sma_360 numeric,
	time_stamp_720 numeric,
	sma_720 numeric,
	time_stamp_1440 numeric,
	sma_1440 numeric
);
```

3.
###trade table that holds executed buy/sell trade information per given strategy
```sql
CREATE TABLE TRADE_TABLE( 
TIME_STAMP timestamp WITHOUT TIMEZONE DEFAULT CURRENT_TIMESTAMP, COIN numeric, BUY_IN numeric,  PROFIT_LOSS numeric, DID_PROFIT boolean, Time_bought char, Strategy_Used char);


```
### To run insertion script (for now at least):
1. Go to the DataBase dir
2. Run `python PriceDataHandler.py` then run `python IndicatorDataWriter.py` to ensure that table properly updates
> If db is set up correctly, this script should work. If it doesn't your table might not be setup correctly.
3. Run `DataBaseDriver.py` to start updating live table values from `CoinAPI`
##CURRENTLY DEBUGGING MULTIPROCESSING 
##TO SEE COIN UPDATES RUN MULTIPLE PROGRAMS FROM `DatabaseSchedule.py`

