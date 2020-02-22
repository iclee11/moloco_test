'''
Using linear regression to fit the data. The R2 is pretty descent, 0.006!

* Fiting results: 
fitted formula: y = -19.29-8.07*x1-1.778012*x2
R2 score: 0.0060532841614568955`
'''

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

# load csv file
df=pd.read_csv('Adops & Data Scientist Sample Data - Q2 Regression.csv')
# setting the matrixes
x, y = df.iloc[:,0:2].values, df.iloc[:,-1].values 
# add constant term for linear regression
x = np.concatenate((np.ones((len(x),1)),x),axis=1)

# Linear Regression using Gradient Descent 
def LinearRegression(x, y, coeff = np.random.rand(1,3), iters = 2000, lr = 0.02):
    for i in range(iters):
        coeff=coeff-(lr/len(x))*np.sum(x*(np.dot(x,coeff.T)-y.reshape((-1,1))), axis=0)
    return coeff.reshape((-1,))

#running the Gradient Descent and cost function
coeff = LinearRegression(x,y) # fit coefficients
print('fitted formula: y = %+.2f%+.2f*x1%+2f*x2' % tuple(coeff))
print('R2 score:',r2_score(y, np.dot(x, coeff.T)))
