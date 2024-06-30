import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

apple = pd.read_csv('data/apple.csv', parse_dates=['Date'])
apple.set_index('Date', inplace=True)
print(apple.loc['2012-8-01':'2013-8-01', 'Close'])

'''
apple.loc['2012-8-01':'2013-8-01', 'Close'].plot(kind='line')
plt.legend(loc='best')
plt.savefig('images/apple.png')
'''

apple['LogReturn'] = np.log(apple['Close'].shift(-1)) - np.log(apple['Close'])
print(apple['LogReturn'])
'''
apple['LogReturn'].hist(bins=50)
plt.savefig('images/apple_hist.png')
'''
