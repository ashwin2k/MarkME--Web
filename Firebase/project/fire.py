'''
Created on Aug 18, 2019

@author: f1
'''
import os
import firebase_admin
import math
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\Python-firebase\mark-me-cebf5-firebase-adminsdk-tkvzz-370d162330.json"
print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
default_app = firebase_admin.initialize_app()
print(default_app.name)
cred = credentials.Certificate('D:\Python-firebase\mark-me-cebf5-firebase-adminsdk-tkvzz-370d162330.json')
actual=[]
to_pred=[]
db = firestore.client()
userref=db.collection(u"Attendance").document(u"CSE A").collection(u"09-Jul-2019")
stud_count=userref.stream()
i=0
for doc in stud_count:
    i=i+1
    # print(u'{} => {}'.format(doc.id, doc.to_dict().get("UID")))
    time= doc.to_dict().get("UID")[11:]
    print("\n"+time)
    actual.append(time[3:5])
    to_pred.append(doc.to_dict().get("BUS"))
    

print("it is")
print(actual)
data=pd.read_csv("checkin.csv")
x=data['ENTRY']
y=data['CHECK IN']
model=LinearRegression()
x=x[:48]
x=x.values.reshape(-1,1)
y=y[:48]
model.fit(x,y)
npa = np.asarray(to_pred, dtype=np.float64)
npa=npa.reshape(-1,1)
print("But we predicted")
pred=model.predict(npa)
print(pred)
lis=pred.tolist()
i=0
print(type(lis))


for a in lis:
    val=math.sqrt((a-int(actual[i]))**2)
    print(val)
    if(val<15):
        print("REJECTED")