import requests
import json
import pandas as pd


def twse_data(r_data: str):
    data = requests.get(
        f'https://www.twse.com.tw/fund/T86?response=json&data={r_data}&selectType=&_=1655704484857')
    print(data.status_code)
    # print(data.text)
    data_json = json.loads(data.text)
    data_store = pd.DataFrame(data_json['data'], columns=data_json['fields'])
    return data_store


# twse_data('20220520')
data = twse_data('20220520')
print(data)
