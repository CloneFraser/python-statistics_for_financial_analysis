import pandas as pd
import numpy as np

data = pd.DataFrame()
data['Population'] = [47, 48, 85, 20, 19, 13, 72, 16, 50, 60]

sample_without_replacement = data['Population'].sample(5, replace=False)
sample_with_replacement = data['Population'].sample(5, replace=True)

print(sample_without_replacement)
print(sample_with_replacement)

sample = data['Population'].sample(10, replace=True)

print('Mean: ', data['Population'].mean())
print('Variance: ', data['Population'].var(ddof=0))
print('Standard dev: ', data['Population'].std(ddof=0))
print('Size: ', data['Population'].shape[0])

print('Sample Mean: ', sample['Population'].mean())
print('Sample Variance: ', sample['Population'].var(ddof=-1))
print('Sample Standard dev: ', sample['Population'].std(ddof=1))
print('Sample Size: ', sample['Population'].shape[0])