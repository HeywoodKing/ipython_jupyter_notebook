import numpy as np
import matplotlib.pyplot as plt

# import mplfinance as mpf
try:
    from mplfinance import candlestick_ohlc
except Exception as ex:
    print(ex)

plt.style.use('ggplot')
plt.figure(figsize=(8, 8))

start_date = '2019-12-01'
end_date = '2020-03-20'

# quotes = quotes_historical_ohlc('INTC', start_date, end_date)
# print(quotes)

quotes = [(1312323, 18.00, 190, 100, 99, 5454545)]
# print(np.random.randint((10, 50, 2)))

dates = np.array([])
volumns = np.array([])

for item in quotes:
    dates = np.append(dates, item[0])
    volumns = np.append(volumns, item[5])

left, width = 0.1, 0.8

rect_vol = [left, 0.1, width, 0.26]
rect_main = [left, 0.4, width, 0.5]

fig = plt.figure()

ax_vol = fig.add_axes(rect_vol)
ax_vol.fill_between(dates, volumns, color='y')
ax_vol.xaxis_date()
plt.setp(ax_vol.get_xticklabels(), rotation=30, horizontalalignment='right')

ax_main = fig.add_axes(rect_main)
ax_main.axes.get_xaxis().set_visible(False)
# 绘制股票K线图
candlestick_ohlc(ax_main, quotes, width=0.6, colorup='r', colordown='g')

ax_main.set_title('Stock INTC Price and Volumn')

plt.show()
