import pandas as pd
import numpy as np
import re
import plotly.express as px

dfsal= pd.read_csv('Code Challenge Data.csv')


dfsal = dfsal[dfsal['salary'].notna()]

dfsal = dfsal[dfsal['salary'] != '-']

dfsal = dfsal.drop_duplicates(subset=['id', 'salary'],keep="first")

dfsal['salary'] = dfsal['salary'].apply(lambda x: x.split('-'))

dfsalFT= pd.DataFrame(dfsal["salary"].to_list())

dfsalFTNum=[dfsalFT.iloc[:, i].str.replace('\D+', '') for i in range (len(dfsalFT.columns))]

dfsalFTNum = pd.DataFrame(dfsalFTNum).T


dfsalFTNum = dfsalFTNum.replace(r'^\s*$', np.nan, regex=True)
dfsalFTNum = dfsalFTNum.fillna(value=np.nan)
dfsalFTNum = dfsalFTNum[dfsalFTNum.isna().all(axis=1)== False]

dfsalFTNum.reset_index(drop=True, inplace=True)


col0 = dfsalFTNum[dfsalFTNum[0].isnull()].index.tolist()
dfsalFTNum.iloc[np.r_[col0],0] = dfsalFTNum.iloc[np.r_[col0],1]
dfsalFTNum.iloc[np.r_[col0],1] = np.nan


col1 = dfsalFTNum[dfsalFTNum[1].isnull()].index.tolist()
dfsalFTNum.iloc[np.r_[col1],1] = dfsalFTNum.iloc[np.r_[col1],2]
dfsalFTNum.iloc[np.r_[col1],2] = np.nan


col2 = dfsalFTNum[dfsalFTNum[2].isnull()].index.tolist()
dfsalFTNum.iloc[np.r_[col2],2] = dfsalFTNum.iloc[np.r_[col2],3]
dfsalFTNum.iloc[np.r_[col2],3] = np.nan


dfsalFTNum = dfsalFTNum.iloc[: , [0,1]]
dfNotNull= dfsalFTNum[(~dfsalFTNum[0].isnull()) & (~dfsalFTNum[1].isnull())]
dfNotNullInt = dfNotNull[[0,1]].astype(np.int64)


dfNotNullInt.reset_index(inplace=True, drop=True)
col0 = dfNotNullInt[0][dfNotNullInt[0]<1000].index.tolist()
dfNotNullInt.iloc[np.r_[col0],0] = dfNotNullInt[0][dfNotNullInt[0]<1000] * 1000

col1 = dfNotNullInt[1][dfNotNullInt[1]<1000].index.tolist()
dfNotNullInt.iloc[np.r_[col1],1] = dfNotNullInt[1][dfNotNullInt[1]<1000] * 1000



dfNotNullInt ["mean"] = dfNotNullInt.mean(axis=1).astype(np.int64)

dfNotNullInt = dfNotNullInt.rename(columns={0: 'salaryFrom', 1: 'salaryTo'})


dfNotNullInt.to_csv("dfNotNullIntResult.csv", index=None)


print(f"\n Count the total number of records===>>> {len(dfNotNullInt)} \n")


print(f'\n Information===>>> \n {dfNotNullInt.info()} \n \n \n')



def describe(df, stats):
    d = df.describe()
    return d.append(df.reindex(d.columns, axis = 1).agg(stats))

print(f"Statistic and Percentile of columns===>>> \n {describe(dfNotNullInt, ['mad'])}")



# Count of countries in all links
figSENDING = px.histogram(dfNotNullInt, x="mean",title="Histogram of salary means")
figSENDING.update_xaxes(type='category')

figSENDING.update_layout(
    title={
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},

font=dict(
        size=14,
        color="RebeccaPurple"))

figSENDING.show()

figSENDING.write_html("salary means.html")



