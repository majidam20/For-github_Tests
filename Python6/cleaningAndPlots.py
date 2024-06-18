### Import Libraries

import pandas as pd
from pathlib import Path
import plotly.express as px
####End of importing libraries


pathCurrrent = Path.cwd()

pathCurrrent = str(pathCurrrent).replace("\\", '/')


dfs = pd.read_csv(pathCurrrent+"/data/SARS-CoV.csv")


dates=["DATE_DRAW", "RECEIVE_DATE", "PROCESSING_DATE"]

 # Find out all the unique values that do not fit the specified format JJJJ-MM-TT
for date in dates:

    m = pd.to_datetime(dfs[date], format='%Y-%m-%d', errors='coerce').isna()

    print (f"\n Unique row values: {dfs.loc[m, date].unique().tolist()} \n")


# Plot a map with the distribution of the labs
diagLab=dfs.groupby(['SENDING_LAB_PC']).size().reset_index(name='counts')

seqLab=dfs.groupby(['SEQUENCING_LAB_PC']).size().reset_index(name='counts')


dfs["SENDING_LAB_PC"]   =    dfs["SENDING_LAB_PC"].round(decimals=0).astype(object)

dfs["SEQUENCING_LAB_PC"]=    dfs["SEQUENCING_LAB_PC"].round(decimals=0).astype(object)



# Create Distribution of the labs
figSENDING = px.histogram(diagLab, x="SENDING_LAB_PC" , y="counts",title="Distribution of the SENDING labs")
figSENDING.update_xaxes(type='category')

figSENDING.update_layout(
    title={
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
figSENDING.show()

figSENDING.write_html("Dist_SENDING_LAB_PC.html")




figseqLab = px.histogram(seqLab, x="SEQUENCING_LAB_PC" , y="counts",title="Distribution of the seqLab labs")
figseqLab.update_xaxes(type='category')

figseqLab.update_layout(
     title={
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
figseqLab.show()

figseqLab.write_html("Dist_SEQUENCING_LAB_PC.html")



print ("Case Study IMS Data Engineer Project finished. \n")









