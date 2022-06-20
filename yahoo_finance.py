import requests
from bs4 import BeautifulSoup


def stock_price(stock: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36',
    }

    data = requests.get(
        f"https://finance.yahoo.com/quote/{stock}?p={stock}", headers=headers)

    if data.status_code == 200:
        soup = BeautifulSoup(data.text, 'lxml')
        # print(soup)
        price = soup.find(
            'fin-streamer', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'})
        price = soup.find('fin-streamer')
        return price.text
        # print(price)
        # print(price.text)
    else:
        print("error = "+data.status_code)
