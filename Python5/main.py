import pandas as pd
from pathlib import Path

pathCurrrent = Path.cwd()

pathCurrrent = str(pathCurrrent).replace("\\", '/')
pathDate = pathCurrrent +  "/Data Challenge/"
pathResults = pathDate + "/Results/"


# Read CSV files
dfacc = pd.read_csv(pathDate + "data_challenge_account.csv")
dfopp = pd.read_csv(pathDate + "data_challenge_opportunity.csv" )
dfoppli = pd.read_csv(pathDate + "data_challenge_opportunity_line_item.csv" )


# Top customers
dfopp.rename(columns={dfopp.columns[1]: 'opportunity_id'}, inplace=True)
dfOppOppli = pd.merge(dfopp,dfoppli, on='opportunity_id')

dfOppOppli1 = dfOppOppli.groupby(by=["account_id"])["account_id"].size().sort_values(ascending=False)
dfOppOppli1 = dfOppOppli1.reset_index(name='amount')
dfOppOppli1.to_csv(pathResults + "topCustomers.csv", index=None)


# Top products
dfoppli = dfoppli.groupby(by=["product_id"])["product_id"].size().sort_values(ascending=False)
dfoppli = dfoppli.reset_index(name="amount")
dfoppli.to_csv(pathResults + "topProducts.csv", index=None)



# Customer structure
dfacc = dfacc.groupby(by=["parent_account"])["id"].count().sort_values(ascending=False).reset_index(name="amount")
dfacc.to_csv(pathResults + "customerStructure.csv", index=None)


# Which products could be recommended to which customers
dfOppOppli = dfOppOppli.groupby(by=["account_id","product_id"])["product_id"].count().sort_values(ascending=False).reset_index(name="amount")
dfOppOppli.to_csv(pathResults + "whichProductsToWhichCustomers.csv", index=None)


print("\n The results as CSV files generated and saved in the folder Results. \n")