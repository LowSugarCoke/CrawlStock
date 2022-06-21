import yfinance as yf

stock = yf.Ticker('2330.TW')
df = stock.history(start="2017-01-01", end="2022-06-20")
print(df)
df_info = stock.info

major_holders = stock.major_holders
print(major_holders)

ins_holders = stock.institutional_holders
print(ins_holders)

# 損益表
fin_data = stock.financials
print(fin_data)

# 資產負債表
balance_data = stock.balance_sheet
print(balance_data)

# 現金流量表
cf_data = stock.cashflow
print(cf_data)