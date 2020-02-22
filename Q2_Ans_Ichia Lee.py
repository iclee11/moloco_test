'''
Using linear regression to fit the data. The R^2 is pretty descent, 0.006!

* Fiting results: 
fitted formula: y = -19.29-8.07*x1-1.778012*x2
R2 score: 0.0060532841614568955
'''

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

df=pd.read_csv('Adops & Data Scientist Sample Data - Q2 Regression.csv', 
               names=['A','B','C'])

#setting the matrixes
x=df.loc[:,['A','B']]
ones = np.ones([x.shape[0],1])
x=np.concatenate((ones,x),axis=1)
y=df.loc[:,'C'].values #converts it from pandas DataFrame to numpy array

#set hyperparameters
alpha=0.02 # learning rate in gradient descent
iters=2000 # num. of iterations
theta = np.random.rand(1,3) # initial guess of the parameters

#create the Gradient Descent 
def Linear_Regression(x,y,theta,iters,alpha):
    for i in range(iters):
        theta=theta-(alpha/len(x))*np.sum(x* 
                (np.dot(x,theta.T)-y.reshape((-1,1))), axis=0)
    return theta.reshape((-1,))

#running the Gradient Descent and cost function
theta_fitted=Linear_Regression(x,y,theta,iters,alpha)
print('fitted formula: y = %+.2f%+.2f*x1%+2f*x2' % tuple(theta_fitted))
print('R2 score:',r2_score(y, np.dot(x, theta_fitted.T)))
