import pandas as pd
import numpy as np
from scipy.stats import norm

apple = pd.read_csv('data/apple.csv')
apple['LogReturn'] = np.log(apple['Close'].shift(-1)) - np.log(apple['Close'])

# 80% cofidence interval - (left = a/2, right = 1-a/2) a = 0.2
z_left = norm.ppf(0.1)
z_right = norm.ppf(0.9)
sample_mean = apple['LogReturn'].mean()
sample_std = apple['LogReturn'].std(ddof=1)/apple.shape[0] ** 0.5

interval_left = sample_mean + z_left * sample_std
interval_right = sample_mean + z_right * sample_std

print('Sample mean: ', sample_mean)
print('80% confidence interval: Left-' + str(interval_left) + ' Right-' + str(interval_right))
