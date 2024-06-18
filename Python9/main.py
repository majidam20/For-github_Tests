import numpy as np
import pandas as pd
from pathlib import Path

pathCurrrent = Path.cwd()

pathCurrrent = str(pathCurrrent).replace("\\", '/')


# Read CSV file
dfsrc = pd.read_csv(pathCurrrent + "/" + "source_1_2_2.csv")

# Solution Task 1
dfsrcNoDup = dfsrc.drop_duplicates(subset=['name','iban'],keep="first")

dfsrcNoDup.to_csv("Task1_dfsrcNoDup.csv", index=None)


# Solution Task 2
similarUniq = np.empty([0,3])
similarNoUniq = np.empty([0,3])
flagUniq = True


for indexi, rowi in dfsrcNoDup.iterrows():
    flagUniq = True

    for indexj, rowj in dfsrcNoDup.iterrows():
        if  rowj["name"].find(rowi["name"]) !=-1  and rowj["id"] not in similarUniq[:,0]:
            if flagUniq == True:
                similarUniq = np.concatenate([similarUniq, np.array(rowj).reshape(1, -1)],axis=0)
                flagUniq = False
            else:
                similarNoUniq = np.concatenate([similarNoUniq, np.array(rowj).reshape(1, -1)],axis=0)

similarNoUniq = pd.DataFrame(similarNoUniq)
similarNoUniq = similarNoUniq.drop_duplicates(subset=[0,1,2],keep="first")


pd.DataFrame(similarUniq).to_csv("Task2_similarUniq.csv", index=None)
similarNoUniq.to_csv("Task2_similarNoUniq.csv", index=None)


print("\n The result CSV files are generated.")
