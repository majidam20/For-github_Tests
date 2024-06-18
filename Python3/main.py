import sys
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
import plotly.express as px


1# Fetch Data of companies from the given link
URL = "https://industrie.de/firmenverzeichnis/"
page = requests.get(URL)

soup1 = BeautifulSoup(page.content, "html.parser")

res1 = soup1.find_all("div", class_="infoservice-result-row")

allContactLst  = []
counter= 0
dfContacts =pd.DataFrame()

for a in res1:
    dicAll = {'globe': [],
              'envelope': [],
              'phone': [],
              'fax': [],
              'group': [],
              'flag': [],
              'money': [],
              'map - pin': []}

# Fetch Data of companies from each page of companies
    linkTemp = a.find('a', href=True)["href"]

    res2 = requests.get(linkTemp)
    soup2 = BeautifulSoup(res2.content)

    soup3 = soup2.findAll('div', attrs={'class': 'textwidget'})
    allContact = soup3[0].findAll('dt', attrs={'class': 'info-icon'})

# Read data from part “Daten und Kontakte”.
    for contact in allContact:

        contactClass = ' '.join(contact.next_element['class'])
        if contactClass == "fa fa-globe" :
                dicAll["globe"].append(contact.nextSibling.text)

        elif contactClass == "fa fa-envelope" :
                    dicAll["envelope"].append(contact.nextSibling.text)

        elif contactClass == "fa fa-phone" :
                    dicAll["phone"].append(contact.nextSibling.text)

        elif contactClass == "fa fa-fax" :
                    dicAll["fax"].append(contact.nextSibling.text)

        elif contactClass == "fa fa-group" :
                    dicAll["group"].append(contact.nextSibling.text)

        elif contactClass == "fa fa-flag" :
                    dicAll["flag"].append(contact.nextSibling.text)

        elif contactClass == "fa fa-money" :
                    dicAll["money"].append(contact.nextSibling.text)

        elif contactClass == "fa fa-map-pin" :
                    dicAll["map - pin"].append(contact.nextSibling.text)

# Append data of each company to a pandas dataframe
    dfContacts = pd.concat([dfContacts,pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dicAll.items() ]))], axis=0)
    counter+=1
    print(f"counter:{counter}")

# Create output CSV file of each company from a pandas dataframe
pd.DataFrame(dfContacts).reset_index(drop=True, inplace=True)
dfContacts.to_csv("dfContacts.csv",index=None)
#sys.exit()


# Read output CSV file of each companies
dfContacts = pd.read_csv('dfContacts.csv')

dfContacts.drop_duplicates(keep='first', inplace=True)
dfContacts.dropna(subset=['globe', 'envelope', 'phone', 'fax' ,'group', 'flag', 'money', 'map - pin' ], how='all', inplace=True)


# Fetch name of european countries in German language
URL = "https://www.colanguage.com/countries-german"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

EUcountriesTable = soup.find("div", class_="table_scrolling_responsive table-responsive")
EUcountries = EUcountriesTable.findAll("span", class_="audio-text")


# Create a list of name of european countries in German language
EUcountriesLst = []
for i in EUcountries:
    EUcountriesLst.append(i.text)

# Calculate count of companies in each EU countries
countryCount = []
for i in EUcountriesLst:
    countryCount.append([i, len(dfContacts[dfContacts['map - pin'].str.contains(i) == True])])



1 # Report1 Count of countries in all links
dfCountryCount = pd.DataFrame(countryCount, columns=['country', 'count']).sort_values(by='count', ascending=False)


# Count of countries in all links
figSENDING = px.bar(dfCountryCount, x="country" , y="count", labels={"country": "Countries"},
                    title="Count of countries in all links", color='country')
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

figSENDING.write_html("dfCountryCount.html")



2# Report2 Maximum number of employees in each EU country
dfGroupEU0 = pd.DataFrame()
for country in EUcountriesLst:
    dfGroupEU1 = dfContacts[(dfContacts['map - pin'].str.contains(country) == True)]
    group = dfGroupEU1.loc[:, 'map - pin'].str.replace('\D+', '')
    dfGroupEU1['group'] = group
    dfGroupEU1['country'] = country
    dfGroupEU0 = pd.concat([dfGroupEU0, dfGroupEU1 ])

dfGroupEU0 = dfGroupEU0.groupby(by='country')['group'].max().reset_index()
dfGroupEU0['group'] = dfGroupEU0['group'].astype(np.int64)
dfGroupEU0 = dfGroupEU0.sort_values(by='group', ascending=False)


# Maximum number of employees in each EU country
figSENDING = px.bar(dfGroupEU0, x="country" , y="group", labels={"country": "Countries", "group": "Employees"},
                    title="Maximum number of employees in each EU country", color='country')
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

figSENDING.write_html("dfGroupEU0.html")




3# Report3 amount of money in each EU country
dfCountryMoney0 = pd.DataFrame()
for country in EUcountriesLst:
    dfCountryMoney1 = dfContacts[(dfContacts['map - pin'].str.contains(country) == True)]
    money = dfCountryMoney1.loc[:, 'money'].str.replace('\D+', '')
    dfCountryMoney1['money'] = money
    dfCountryMoney1['country'] = country
    dfCountryMoney0 = pd.concat([dfCountryMoney0, dfCountryMoney1])

dfCountryMoney0 = dfCountryMoney0[dfCountryMoney0['money'].notna()]
dfCountryMoney0['money'] = dfCountryMoney0['money'].astype(np.int64)
dfCountryMoney0 = dfCountryMoney0.groupby(by='country')['money'].mean().reset_index().sort_values(by='money', ascending=False)


# Amount of money in each EU country
figSENDING = px.bar(dfCountryMoney0, x="country" , y="money", labels={"country": "Countries", "money": "Money"},
                    title="Amount of money in each EU country", color='country')
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

figSENDING.write_html("dfCountryMoney0.html")




4# Report4 Mean of money in each EU country equal and after year 1900
dfCountryFlag0 = pd.DataFrame()
for country in EUcountriesLst:
    dfCountryFlag1 = dfContacts[(dfContacts['map - pin'].str.contains(country) == True)]
    flag = dfCountryFlag1.loc[:, 'flag'].str.replace('\D+', '')
    dfCountryFlag1['flag'] = flag
    dfCountryFlag1['country'] = country
    dfCountryFlag0 = pd.concat([dfCountryFlag0, dfCountryFlag1])

dfCountryFlag0 = dfCountryFlag0[dfCountryFlag0['flag'].notna()]
dfCountryFlag0 = dfCountryFlag0[dfCountryFlag0['money'].notna()]
dfCountryFlag0['flag'] = dfCountryFlag0.loc[:, 'flag'].str.replace('\D+', '')
dfCountryFlag0['money'] = dfCountryFlag0.loc[:, 'money'].str.replace('\D+', '')

dfCountryFlag0['flag'] = dfCountryFlag0['flag'].astype(np.int64)

dfCountryFlag0 = dfCountryFlag0[dfCountryFlag0['flag'] < 2025]

dfCountryFlag0U1900 = dfCountryFlag0[dfCountryFlag0['flag'] < 1900].groupby(by='country')['money'].mean()
dfCountryFlag0A1900 = dfCountryFlag0[dfCountryFlag0['flag'] >= 1900].groupby(by='country')['money'].mean().reset_index().sort_values(by='money', ascending=False)


# Mean of money in each EU country equal and after year 1900
figSENDING = px.bar(dfCountryFlag0A1900, x="country" , y="money", labels={"country": "Countries", "money": "Money"},
                    title="Mean of money in each EU country equal and after year 1900", color='country')
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

figSENDING.write_html("dfCountryFlag0A1900.html")







