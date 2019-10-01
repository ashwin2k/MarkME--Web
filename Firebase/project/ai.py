'''
Created on Aug 18, 2019

@author: f1
'''
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
data=pd.read_csv("checkin.csv")
print(data.shape)
x=data['ENTRY']
y=data['CHECK IN']
model=LinearRegression()
x=x[:48]
x=x.values.reshape(-1,1)
y=y[:48]
model.fit(x,y)
to_predict=[data['ENTRY'][50],'43',30]
npa = np.asarray(to_predict, dtype=np.float64)
npa=npa.reshape(-1,1)
print(model.predict(npa))


# In[ ]:




