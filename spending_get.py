import requests
import json
import pandas as pd
from pandas import json_normalize
import xlwt

try:
    API_ENDPOINT = "http://api.spending.gov.ua/api/v2/api/transactions/"
    list_in = pd.read_excel("bm90.xlsx")
    df_all = pd.DataFrame()
    headers = {
    'accept': 'application/json',
    }

    for i, tin in enumerate(list_in['TIN']):
        params = (
        ('payers_edrpous', str('{:08d}'.format(tin))),
        ('startdate', '2020-01-01'),
        ('enddate', '2020-02-21'),
        ('purpose', '2111'),
        )
        r = requests.get(API_ENDPOINT, headers=headers, params=params)
        raw_data = r.text
        df = json_normalize(json.loads(raw_data))
        df_all = df_all.append(df)
        print(str('{:08d}'.format(tin)))
        print(df.info)
        print(df.shape)
        del df

finally:
    df_all.to_excel("zp_budget.xlsx")






