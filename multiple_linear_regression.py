import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import statsmodels.formula.api as smf

def adjustedMetric(data, model, model_k, yname):
    data['yhat'] = model.predict(data)
    sst = ((data[yname] - data[yname].mean())**2).sum()
    ssr = ((data['yhat'] - data[yname].mean())**2).sum()
    sse = ((data[yname] - data['yhat'])**2).sum()
    r2 = ssr/sst
    adjust_r2 = 1-(1-r2) * (data.shape[0]-1)/(data.shape[0]-model_k-1)
    rmse = (sse/(data.shape[0]-model_k-1))**0.5
    return adjust_r2, rmse


aord = pd.read_csv('data/ALLOrdinary.csv')

nikkei = pd.read_csv('data/Nikkei225.csv')
hsi = pd.read_csv('data/HSI.csv')

daxi = pd.read_csv('data/DAXI.csv')
cac40 = pd.read_csv('data/CAC40.csv')

sp500 = pd.read_csv('data/SP500.csv')
dji = pd.read_csv('data/DJI.csv')
nasdaq = pd.read_csv('data/nasdaq_composite.csv')

spy = pd.read_csv('data/SPY.csv', parse_dates=True)

indicepanel = pd.DataFrame(index=spy.index)

indicepanel['spy'] = spy['Open'].shift(-1) - spy['Open']
indicepanel['spy_lag1'] = indicepanel['spy'].shift(1)

indicepanel['sp500'] = sp500['Open'] - sp500['Open'].shift(1)
indicepanel['nasdaq'] = nasdaq['Open'] - nasdaq['Open'].shift(1)
indicepanel['dji'] = dji['Open'] - dji['Open'].shift(1)

indicepanel['cac40'] = cac40['Open'] - cac40['Open'].shift(1)
indicepanel['daxi'] = daxi['Open'] - daxi['Open'].shift(1)

indicepanel['aord'] = aord['Close'] - aord['Open']
indicepanel['hsi'] = hsi['Close'] - hsi['Open']
indicepanel['nikkei'] = nikkei['Close'] - nikkei['Open']

indicepanel['Price'] = spy['Open']

indicepanel = indicepanel.ffill()
indicepanel = indicepanel.dropna()

indicepanel.to_csv('data/indicepanel.csv')

train = indicepanel.iloc[-2000:-1000, :]
test = indicepanel.iloc[-1000:, :]

sm = scatter_matrix(train, figsize=(10, 10))
plt.show()

formula = 'spy ~ spy_lag1+sp500+nasdaq+dji+cac40+daxi+aord+nikkei+hsi'
lm = smf.ols(formula=formula, data=train).fit()

train['PredictedY'] = lm.predict(train)
test['PredictedY'] = lm.predict(test)

plt.scatter(train['spy'], train['PredictedY'])
plt.show()

print('adjusted R2 and RMSE on Train: ', adjustedMetric(train, lm, 9, 'spy'))
print('adjusted R2 and RMSE on Test: ', adjustedMetric(test, lm, 9, 'spy'))

# Evaluating model and strategy
train['order'] = [1 if signal > 0 else -1 for signal in train['PredictedY']]
train['profit'] = train['spy']*train['order']

train['wealth'] = train['profit'].cumsum()
print('Total Profit in train: ', train['profit'].sum())







