### Import Libraries

import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
import warnings
####End of importing libraries

warnings.filterwarnings("ignore")

pathCurrrent = Path.cwd()

pathCurrrent = str(pathCurrrent).replace("\\", '/')


dfCompAct = pd.read_excel("companies-taking-action.xlsx")



# Total number of nans (all coulumn values being nan)
idx = dfCompAct.index[dfCompAct.isnull().all(1)]
nans = dfCompAct.iloc[idx]
print(f"\nTotal number of nans (all coulumn values being nan): {len(nans)}\n")



# Return row number of rows having a special unknown character 'Ø'
dfCompAct[dfCompAct.apply(lambda x: x.str.contains('Ø')).any(axis=1)==True].index.values


# Replace special character with empty character
dfCompAct.replace({'Ø': ''}, regex=True)


# Replace nan date with a value '00/00/0000'
dfCompAct[["BA1.5 Date", "Date"]]= dfCompAct[["BA1.5 Date", "Date"]].fillna('00/00/0000')


# Replace all nan values in table with empty character
dfCompAct.fillna('', inplace=True)


# Doing a table normalization technique, and creating 3 new tables
dfCompActTarget=dfCompAct.loc[:,['Company Name', 'Near term - Target Status', 'Near term - Target Classification' ,'Near term - Target Year', 'Long term - Target Status', 'Long term - Target Classification', 'Long term - Target Year', 'Target Classification']]


dfCompActMain=dfCompAct.loc[:,['Company Name', 'ISIN', 'LEI', 'Organization Type', 'Net-Zero Committed' ,'Net-Zero Year', 'BA1.5', 'BA1.5 Date', 'Sector', 'Date', 'Extension']]


dfCompActLoc=dfCompAct.loc[:,['Company Name', 'Location', 'Region']]


# Insert datasets to database, root, password, and codetest may different with your connection configurations
engine = create_engine('mysql+pymysql://root:1333@localhost/codetest') # Enter your password and database names here


dfCompActTarget.to_sql('tbCompActTarget',con=engine,index=False,if_exists='append')
print("\nData is saved in table tbCompActTarget")



dfCompActMain.to_sql('tbCompActMain',con=engine,index=False,if_exists='append')
print("\nData is saved in table tbCompActMain")


dfCompActLoc.to_sql('tbCompActLoc',con=engine,index=False,if_exists='append')
print("\nData is saved in table tbCompActLoc")



print("\n Task 2 cleaning and normalization of tables are done!!! \n")





