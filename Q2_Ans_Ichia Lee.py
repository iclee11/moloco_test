import numpy as np
import pandas as pd

df=pd.read_csv('Adops & Data Scientist Sample Data - Q2 Regression.csv', 
               names=['A','B','C'])

#normalize the data
df=(df-df.mean())/df.std()

#setting the matrixes
x=df.loc[:,['A','B']]
ones = np.ones([x.shape[0],1])
x=np.concatenate((ones,x),axis=1)

y=df.loc[:,'C'].values #converts it from pandas DataFrame to numpy array
theta = np.zeros([1,3])

#set hyperparameters
alpha=0.02
iters=2000

#create the Gradient Descent 
def Gradient_Descent(x,y,theta,iters,alpha):
    for i in range(iters):
        theta=theta-(alpha/len(x))*np.sum(x* 
                        (np.dot(x,theta.T)-y.reshape((-1,1))), axis=0)
    return theta

#running the Gradient Descent and cost function
result=Gradient_Descent(x,y,theta,iters,alpha)
print('result:', result)

#Validate by sklearn
from sklearn.linear_model import LinearRegression
model=LinearRegression()
x_model=df[['A','B']]
y_model=df['C']
model.fit(x_model,y_model)
print('intercept:',model.intercept_)
print('coefficient:',model.coef_)

