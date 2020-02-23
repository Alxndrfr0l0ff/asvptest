import requests
import json
import pandas as pd
from pandas import json_normalize
import xlwt


API_ENDPOINT = "http://api.spending.gov.ua/api/v2/api/transactions/"

headers = {
    'accept': 'application/json',
}

params = (
    ('payers_edrpous', '40312499'),
    ('startdate', '2020-02-01'),
    ('enddate', '2020-02-21'),
    ('purpose', '2111'),
)

r = requests.get(API_ENDPOINT, headers=headers, params=params)
raw_data = r.text
df = json_normalize(json.loads(raw_data))
df.to_excel("tr_40312499.xls")




