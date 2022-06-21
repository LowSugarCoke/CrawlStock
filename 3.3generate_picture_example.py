import ta
import yfinance as yf
import pandas as pd
import mpl_finance as mpf
import matplotlib.pyplot as plt

stock = yf.Ticker('2330.TW')
df = stock.history(start="2020-01-01", end="2022-06-20")

# 呼叫布林通道
indicator_bb = ta.volatility.BollingerBands(
    close=df["Close"], window=20, window_dev=2)
# 呼叫布林中線
df['bbm'] = indicator_bb.bollinger_mavg()
# 呼叫布林上線
df['bbh'] = indicator_bb.bollinger_hband()
# 布林下線
df['bbl'] = indicator_bb.bollinger_lband()


fig = plt.figure(figsize=(24, 8))
grid = plt.GridSpec(3, 20)
ax = fig.add_subplot(grid[0:2, 1:])
ax2 = fig.add_subplot(grid[2:, 1:])

# 在ax區塊上畫上布林上中下
ax.plot(df['bbm'].values, color='b', label=' bbm')
ax.plot(df['bbh'].values, color='g', label=' bbh')
ax.plot(df['bbl'].values, color='r', label=' bbl')


# mpf.candlestick2_ochl(ax, df['Open'], df['Close'], df['High'],
#                       df['Low'], width=0.6, colorup='r', colordown='g', alpha=0.75)

# 設置圖片標題

mpf.candlestick2_ochl(ax, df['Open'], df['Close'], df['High'],
                      df['Low'], width=0.6, colorup='r', colordown='g', alpha=0.75)
mpf.volume_overlay(ax2, df['Open'], df['Close'],
                   df['Volume'], colorup='r', colordown='g')

convert_date = pd.DataFrame(df.index[::30])['Date'].apply(
    lambda x: x.strftime('%Y-%m-%d'))
print(convert_date)

ax.set_xticks(range(0, len(df.index), 30))
ax.set_xticklabels(convert_date, rotation=90)
ax2.set_xticks(range(0, len(df.index), 30))
ax2.set_xticklabels(convert_date, rotation=90)

plt.title(f'2330.TW Stock Price')
plt.xlabel('Date')
plt.ylabel("Price")

# 防止重疊
fig.tight_layout()
# 設置legend才會有label跑出來
ax.legend()
# 儲存圖片檔為png
plt.savefig('test.png')

# plt.legend(loc='best')
plt.show()
