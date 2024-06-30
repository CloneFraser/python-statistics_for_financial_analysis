import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fst_sample = pd.DataFrame(np.random.normal(10, 5, size=30))
print(fst_sample)
print('Sample Mean: ', fst_sample[0].mean())
print('Sample SD: ', fst_sample[0].std(ddof=1))

mean_list = []
var_list = []

for x in range(1000):
    sample = pd.DataFrame(np.random.normal(10, 5, size=30))
    mean_list.append(sample[0].mean())
    var_list.append(sample[0].std(ddof=1))

collection = pd.DataFrame()
collection['mean_list'] = mean_list
collection['var_list'] = var_list

print(collection)

collection['mean_list'].hist(bins=500)
plt.savefig('images/means.png')

