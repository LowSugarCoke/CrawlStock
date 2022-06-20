import yfinance as yf

stock = yf.Ticker('2330.TW')
df = stock.history(start="2017-01-01", end="2022-06-20")
print(df)
df_info = stock.info

major_holders = stock.major_holders
print(major_holders)

ins_holders = stock.institutional_holders
print(ins_holders)

fin_data = stock.financials
print(fin_data)

balance_data = stock.balance_sheet
print(balance_data)
