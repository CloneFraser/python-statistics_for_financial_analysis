import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fb = pd.read_csv('data/facebook.csv')
ms = pd.read_csv('data/microsoft.csv')

print()
print(fb.head())
print(fb['Open'])
print(fb.loc[1:252, ['Date', 'Close']])
print(fb.iloc[1, 4])

#fb.loc[1:252, 'Close'].plot(kind='line')
#plt.savefig('images/facebook.png')

fb['PriceDiff'] = fb['Close'] - fb['Open']
fb['Average3'] = (fb['Close'] + fb['Close'].shift(1) + fb['Close'].shift(2))/3
fb['MA40'] = fb['Close'].rolling(window=40).mean()
fb['MA200'] = fb['Close'].rolling(window=200).mean()
print(fb.tail())

fb['Close'].plot(kind='line').legend(loc='upper left')
fb['MA40'].plot(kind='line').legend(loc='upper left')
fb['MA200'].plot(kind='line').legend(loc='upper left')
plt.savefig('images/facebook_moving_average.png')

