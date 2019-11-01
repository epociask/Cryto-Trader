# Crypto Trader

### Setting up the local database:
1. Make sure postgresql is installed
2. Start the postgres local server via `pg_ctl -D /usr/local/var/postgres start` on mac
3. Start the postgres shell: `psql -U postgres`
4. Create the database. Looks like this for now:

### Generic Price Data Table DLL
```sql
CREATE TABLE bitcoin_price_data (
    day_volume numeric,
    price numeric,
    market_cap numeric,
    time_stamp timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
```

### Generic Indicator Data Table DLL
```sql
CREATE TABLE bitcoin_indicators (
    sma_1 integer,
    sma_5 integer,
    sma_10 integer,
    sma_30 integer
);
```

### To run insertion script (for now at least):
1. Go to the DataBase dir
2. Run `python PriceDataHandler.py`
> If db is set up correctly, this script should work. If it doesn't your table might not be setup correctly.