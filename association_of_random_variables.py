import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

housing = pd.read_csv('data/housing.csv', index_col=0)

print(housing.cov())
print(housing.corr())

sm = scatter_matrix(housing, figsize=(10, 10))
plt.savefig('images/housing_scatter_matrix.png')
