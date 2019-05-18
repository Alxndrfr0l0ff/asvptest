import requests
import json
import pandas as pd
from pandas.io.json import json_normalize

API_ENDPOINT = "https://asvpweb.minjust.gov.ua/listDebtCredVPEndpoint"

headers = {"Content-Type": "application/json"}
data_in = {
    "searchType": "22",
    "filter": {
        "VPNum": "",
        "vpOpenFrom": "2019-05-17T00:00:00.000Z",
        "vpOpenTo": "2019-05-17T20:59:59.000Z",
        "debtFilter": {
            "FirmName": "",
            "FirmEdrpou": ""
        },
        "creditFilter": {
            "FirmName": "",
            "FirmEdrpou": "39394463"
        }
    }
}

r = requests.post(url=API_ENDPOINT, data=json.dumps(data_in), headers=headers)
raw_data = r.text
data = json.loads(raw_data)
df = pd.DataFrame(json_normalize(data=data['results'], record_path='debtors',
                                 meta=['vdID', 'orderNum', 'mi_wfStateWithError', 'depID', 'depStr', 'beginDate']))

print(df)
