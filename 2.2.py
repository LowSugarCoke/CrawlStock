import pandas as pd
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36',
}

html_data = requests.get(
    "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2", headers=headers)
if html_data.status_code == 200:
    # print(html_data.text)
    x = pd.read_html(html_data.text)
    # print(x)
    # print(type(x))
    # print(len(x))
    x = x[0]
    x.columns = x.iloc[0, :]
    x = x.iloc[1:, :]
    print(x)
    print(x.columns)
    x['代號'] = x['有價證券代號及名稱'].apply(lambda x: x.split()[0])
    x['股票名稱'] = x['有價證券代號及名稱'].apply(lambda x: x.split()[-1])

    # print(x)

    # 將無法轉換成datatime的資料變成Nan
    x['上市日'] = pd.to_datetime(x['上市日'], errors='coerce')
    # 去掉Nan的資料
    x = x.dropna(subset=['上市日'])
    print(x)

    # 去掉不需要的資料
    x = x.drop(['有價證券代號及名稱', '國際證券辨識號碼(ISIN Code)', 'CFICode', '備註'], axis=1)
    # 更換順序
    x = x[['代號', '股票名稱', '上市日', '市場別', '產業別']]

    print(x)

    # 去掉產業別為空的資料
    x = x.dropna(subset=['產業別'])

    # str.isdigit()函數, 確認是不是數字
    x = x[x["代號"].str.isdigit()]

    x.to_excel('stock_list.xlsx')


else:
    print(html_data.status_code)
