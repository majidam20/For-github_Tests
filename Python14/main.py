# Import Libraries
import pandas as pd
import numpy as np
from pycoingecko import CoinGeckoAPI
from sqlalchemy import create_engine
import sqlalchemy
from pathlib import Path


try:
    # Create an instance of the CoinGeckoAPI class and assigns it to the variable cg
    cg = CoinGeckoAPI() # connect

    # Check API connectivity using ping method
    print("\nSuccessfully connected to the CoinGeckoAPI\n")


    all_crypto_data =pd.DataFrame()


    #  I only Retrieved data from page 1 to 3 for Bitcoin (BTC) from the CoinGecko API
    for i in range(1,4):
        data = cg.get_coins_markets(vs_currency ="eur",page=i, order="market_cap_dec", include_24hr_change=True)# eur

        # Convert the current page of data into a DataFrame
        page_crypto_data = pd.DataFrame(data)

        # Append the current page's data to the overall DataFrame
        all_crypto_data = pd.concat([all_crypto_data, page_crypto_data], ignore_index=True)


    # Sort data based on last_updated column descending order
    all_crypto_data.sort_values("last_updated",ascending=False)


    # Doing some cleaning solutions
    # Replace all nan values in table with Zero
    all_crypto_data.dropna(how='all', inplace=True)
    all_crypto_data.fillna(0, inplace=True)
    all_crypto_data['roi'] = all_crypto_data['roi'].astype(str)
    all_crypto_data.drop_duplicates(keep='first', inplace=True)




    # Convert current_price in Euro to US Dollar
    all_crypto_data["current_price_US"] = all_crypto_data["current_price"] * 1.09
    all_crypto_data = all_crypto_data.rename(columns={'current_price': 'current_price_EU'})
    my_column = all_crypto_data.pop('current_price_US')
    all_crypto_data.insert(5, my_column.name, my_column)


    # Reform date to format %d-%m-%Y %H:%M:%S
    all_crypto_data["last_updated"] = pd.to_datetime(all_crypto_data["last_updated"], errors='coerce',utc=False).dt.strftime('%d-%m-%Y %H:%M:%S')
    all_crypto_data["ath_date"] = pd.to_datetime(all_crypto_data["ath_date"], errors='coerce',utc=False).dt.strftime('%d-%m-%Y %H:%M:%S')
    all_crypto_data["atl_date"] = pd.to_datetime(all_crypto_data["atl_date"], errors='coerce',utc=False).dt.strftime('%d-%m-%Y %H:%M:%S')


    # Calculate increment percentage value change in last 24 hours
    high = all_crypto_data[['current_price_EU','high_24h']].pct_change(axis=1)['high_24h']

    # Calculate decrement percentage value change in last 24 hours
    low = all_crypto_data[['current_price_EU','low_24h']].pct_change(axis=1)['low_24h']

    # Calculate average percentage value change in last 24 hours
    all_crypto_data["AVG_change(high_low)"] = (high + low) / 2


    # Put new column after percentage High and Low columns
    my_column = all_crypto_data.pop('AVG_change(high_low)')
    all_crypto_data.insert(13, my_column.name, my_column)


    # Convert total_volume from float to int64
    all_crypto_data["total_volume"] = all_crypto_data["total_volume"].astype(np.int64)


except Exception as ex:
    print(f'Sorry failed to connect API: {ex}')


pathCurrrent = Path.cwd()
pathCurrrent = str(pathCurrrent).replace("\\", '/')

# Read database configuration from dbConfigs.txt file
dbConfigs = pd.read_csv(pathCurrrent + "/dbConfigs.txt")



# Connect to database with dbConfigs data
engine = create_engine(f"postgresql+psycopg2://{dbConfigs.loc[0,'user']}:{dbConfigs.loc[0,'password']}@{dbConfigs.loc[0,'host']}/{dbConfigs.loc[0,'dbname']}")

try:
    with engine.connect() as connection_str:
        print('Successfully connected to the PostgreSQL database')

    # Check If the table already was existed or not
    if sqlalchemy.inspect(engine).has_table("all_crypto_data") == False:

        # Create table and Insert all_crypto_data to database as a new table
        all_crypto_data.to_sql('all_crypto_data', con=engine, index=False )
        print("\nData is saved in table all_crypto_data")

    else:
        print("\nTable all_crypto_data was already created!")


except Exception as ex:
    print(f'Sorry failed to connect: {ex}')



