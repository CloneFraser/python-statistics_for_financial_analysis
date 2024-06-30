import pandas as pd
import matplotlib.pyplot as plt

fb = pd.read_csv('data/facebook.csv')
ms = pd.read_csv('data/microsoft.csv')

ms['MA10'] = ms['Close'].rolling(10).mean()  # Fast Signal
ms['MA50'] = ms['Close'].rolling(50).mean()  # Slow Signal

'''
ms['Close'].plot(legend=True)
ms['MA10'].plot(legend=True)
ms['MA50'].plot(legend=True)
plt.savefig('images/simple_trading_strat.png')
'''

ms['Shares'] = [1 if ms.loc[ei, 'MA10'] > ms.loc[ei,'MA50'] else 0 for ei in ms.index]
ms['Close1'] = ms['Close'].shift(-1)
ms['Profit'] = [ms.loc[ei, 'Close1'] - ms.loc[ei, 'Close'] if ms.loc[ei, 'Shares'] else 0 for ei in ms.index]
ms['Wealth'] = ms['Profit'].cumsum()

ms['Profit'].plot(legend=True)
ms['Wealth'].plot(legend=True)
plt.savefig('images/simple_trading_strat_profit&wealth.png')

print(ms)

