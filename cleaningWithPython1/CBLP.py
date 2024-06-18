### Import Libraries
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import sys
import random
import pandas as pd
import numpy as np

np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(threshold=np.inf)

os.environ['PYTHONHASHSEED'] = '0'
np.random.seed(42)
random.seed(12345)


import warnings
warnings.filterwarnings("ignore")


####End of importing libraries


from pathlib import Path
pathCurrrent = Path.cwd()


pathCurrrent = str(pathCurrrent).replace("\\", '/')

pathPlots = pathCurrrent + "/plots/"
pathData = pathCurrrent + "/data/"
dfRe = pd.read_csv(pathData+"case_study_requests.csv", delimiter=";")
dfSh = pd.read_csv(pathData+"case_study_shifts.csv", delimiter=";")


dfRe=dfRe[pd.to_datetime(dfRe["requested_at"]).dt.year==2030]


dfRide_fare=dfRe.groupby(by=["user_id","final_status"]).sum()['ride_fare'].reset_index().sort_values('ride_fare', ascending=False).reset_index(drop=True)



dfCmp=dfRe.groupby(by=["user_id"])["final_status"].apply(lambda x: (x=='completed').sum()).reset_index().sort_values('final_status', ascending=False)
dfCmp = dfCmp.rename(columns={'final_status': 'FS_completed'})
dfRide_fare_dfCmp= pd.merge(dfRide_fare,dfCmp, on="user_id")



dfRDO=dfRe.groupby(by=["user_id"])["final_status"].apply(lambda x: (x=='rider_declined_offer').sum()).reset_index().sort_values('final_status', ascending=False)
dfRDO = dfRDO.rename(columns={'final_status': 'FS_RDO'})
dfRide_fare_dfCmp_RDO=pd.merge(dfRide_fare_dfCmp,dfRDO, on="user_id")



dfNO=dfRe.groupby(by=["user_id"])["final_status"].apply(lambda x: (x=='no_offer').sum()).reset_index().sort_values('final_status', ascending=False)
dfNO = dfNO.rename(columns={'final_status': 'FS_NO'})
dfRide_fare_dfCmp_RDO_dfNO=pd.merge(dfRide_fare_dfCmp_RDO,dfNO, on="user_id")



dfNS=dfRe.groupby(by=["user_id"])["final_status"].apply(lambda x: (x=='no show').sum()).reset_index().sort_values('final_status', ascending=False)
dfNS = dfNS.rename(columns={'final_status': 'FS_NS'})
dfRide_fare_dfCmp_RDO_dfNO_dfNS=pd.merge(dfRide_fare_dfCmp_RDO_dfNO,dfNS, on="user_id")



dfcityA= dfRe.groupby(by=["user_id"])["city"].apply(lambda x: (x=='A').sum()).reset_index().sort_values('city', ascending=False)
dfcityA = dfcityA.rename(columns={'city': 'cityA'})
dfRide_fare_dfCmp_RDO_dfNO_dfNS_CA=pd.merge(dfRide_fare_dfCmp_RDO_dfNO_dfNS,dfcityA, on="user_id")



dfcityB= dfRe.groupby(by=["user_id"])["city"].apply(lambda x: (x=='B').sum()).reset_index().sort_values('city', ascending=False)
dfcityB = dfcityB.rename(columns={'city': 'cityB'})
dfRide_fare_dfCmp_RDO_dfNO_dfNS_CA_CB=pd.merge(dfRide_fare_dfCmp_RDO_dfNO_dfNS_CA,dfcityB, on="user_id")



dfRide_fare_dfCmp_RDO_dfNO_dfNS_CA_CB= dfRide_fare_dfCmp_RDO_dfNO_dfNS_CA_CB.drop_duplicates(['user_id'])
dfRide_fare_dfCmp_RDO_dfNO_dfNS_CA_CB= dfRide_fare_dfCmp_RDO_dfNO_dfNS_CA_CB.drop(['final_status'], axis=1)


dfRide_fare_dfCmp_RDO_dfNO_dfNS_CA_CB.to_csv("dfRide_fare_dfCmp_RDO_dfNO_dfNS_CA_CB.csv", index=False)


print("The file dfRide_fare_dfCmp_RDO_dfNO_dfNS_CA_CB.csv that contains analytical results of the case study was generated.")





