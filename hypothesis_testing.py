import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

apple = pd.read_csv('data/apple.csv', parse_dates=True)
apple.set_index('Date', inplace=True)

apple['LogReturn'] = np.log(apple['Close'].shift(-1)) - np.log(apple['Close'])

print(apple)

'''
plt.title('Close Price of Apple Stock 2007-2018')
plt.xlabel('Time')
plt.ylabel('US Dollar ($)')
plt.plot(apple.loc[:, 'Close'])
plt.savefig('images/apple_close.png')
'''

'''
plt.title('Daily Return of Apple Stock 2007-2018')
plt.xlabel('Time')
plt.ylabel('US Dollar ($)')
plt.plot(apple.loc[:, 'LogReturn'])
plt.savefig('images/apple_return.png')
'''

# Standardisation (Z Distribution)
mean = apple['LogReturn'].mean()
std = apple['LogReturn'].std(ddof=1)
n = apple['LogReturn'].shape[0]
z_dist = (mean - 0)/(std/(n**0.5))
print(z_dist)

# Two Tail test at significance level 0.05
alpha = 0.05
zleft = norm.ppf(alpha/2, 0, 1)
zright = -zleft

print(zleft, zright)

