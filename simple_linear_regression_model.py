import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

housing = pd.read_csv('data/housing.csv', index_col=0)


b0 = 1
b1 = 2
housing['GuessResponse'] = b0 + b1*housing['RM']
housing['ObservedError'] = housing['MEDV'] - housing['GuessResponse']

'''
indices = [7, 20, 100]
print(housing['ObservedError'].loc[indices])
print('Sum of squared error is: ', (housing['ObservedError']**2).sum())
'''

model = smf.ols(formula='MEDV~RM', data=housing).fit()
print(model.summary())

b0 = model.params['Intercept']
b1 = model.params['RM']
housing['BestResponse'] = b0 + b1*housing['RM']

'''
plt.scatter(housing['RM'], housing['MEDV'], color='g', label='Real')
plt.plot(housing['RM'], housing['GuessResponse'], color='red')
plt.plot(housing['RM'], housing['BestResponse'], color='yellow')
plt.xlabel('RM')
plt.ylabel('MEDV')
plt.legend()
plt.savefig('images/simple_linear_regression_model')
'''





