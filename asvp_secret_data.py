import requests
import json
import pandas as pd
from pandas.io.json import json_normalize

API_ENDPOINT = "https://asvpweb.minjust.gov.ua/SptDataPEndpoint"

headers = {"Content-Type": "application/json; charset=UTF-8"}

data_in = {"filter": {"VpNum": '60507172', "SecretNum": "А2069ВВ3В4ЕВ", "dataType": "getSharedInfoByVP"}}

r = requests.post(url=API_ENDPOINT, data=json.dumps(data_in), headers=headers)
raw_data = r.text
data = json.loads(raw_data)
