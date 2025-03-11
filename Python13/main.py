import requests
import pandas as pd
import io
import json

import freshsales
from freshsales.api import API
response = API('https://dataengineertechnicalexercise.freshchat.com/v2/accounts/', 'VpQuG1SSj-Uo4GrwCldXQw')

headers = {
     'content-type': 'application/json',
     'accept': 'application/json',
     'Authorization': 'Token token=VpQuG1SSj-Uo4GrwCldXQw'
}
headers = headers
response = requests.get("https://dataengineertechnicalexercise.freshchat.com/v2/users/fetch", headers)

print(response.status_code)

if (
    response.status_code == 200 and
    response.headers["content-type"].strip().startswith("application/json")
):
    try:
        response.json()
    except ValueError:
        pass

#print(pd.read_csv(io.StringIO(response.content.decode('utf-8'))))
data = response.json()


print(data)

