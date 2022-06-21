import pandas as pd
import yfinance as yf


def mine_add_all_features(df: pd.DataFrame):
    # rolling以6為單位位移並取最大值
    df['Highest_high'] = df['High'].rolling(6).max()
    # rolling以6為單位位移並取最小值
    df['Lowest_low'] = df['Low'].rolling(6).min()

    # 一樣用6根作為rolling，並且設計計算函數第一個值減去最後一個值
    O_C_high = df['High'].rolling(6).apply(lambda x: x[0]-x[-1])
    df['OCHIGH'] = O_C_high

    return df


stock = yf.Ticker('2330.TW')
df = stock.history(start="2017-01-01", end="2021-02-02")
df = mine_add_all_features(df)
# 存成Excel
df.to_excel(r'final.xlsx')
