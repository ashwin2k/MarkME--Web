import os
import firebase_admin
import math
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np
import pandas as pd
import smtplib

import imutils
import pickle
import cv2
from sklearn.linear_model import LinearRegression

from flask import Flask
from flask.templating import render_template
from src.fire import default_app

app = Flask(__name__)
@app.route('/fr')
def face():
    your_list=[]

    print("[INFO] loading face detector...")
    people=[]
    protoPath = os.path.sep.join(["face_detection_model", "deploy.prototxt"])
    modelPath = os.path.sep.join(["face_detection_model",
        "res10_300x300_ssd_iter_140000.caffemodel"])
    detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)
    
    print("[INFO] loading face recognizer...")
    embedder = cv2.dnn.readNetFromTorch("openface_nn4.small2.v1.t7")
    
    recognizer = pickle.loads(open("output/recognizer.pickle", "rb").read())
    le = pickle.loads(open("output/le.pickles", "rb").read())
    
    
    image = cv2.imread("images/a.jpg")
    image = imutils.resize(image, width=600)
    (h, w) = image.shape[:2]
    
    imageBlob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 1.0, (300, 300),
        (104.0, 177.0, 123.0), swapRB=False, crop=False)
    
    
    detector.setInput(imageBlob)
    detections = detector.forward()
    
    for i in range(0, detections.shape[2]):
        
        confidence = detections[0, 0, i, 2]
    
        if confidence >0.7:
        
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        face = image[startY:endY, startX:endX]
        

        faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96),
            (0, 0, 0), swapRB=True, crop=False)
        embedder.setInput(faceBlob)
        vec = embedder.forward()

        preds = recognizer.predict_proba(vec)[0]
        j = np.argmax(preds)
        name = le.classes_[j]
        people.append(name)
    print(people)
    

    return render_template('index.html', your_list=your_list)

        

@app.route('/AI')
def predict():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\Python-firebase\mark-me-cebf5-firebase-adminsdk-tkvzz-370d162330.json"
    print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate('D:\Python-firebase\mark-me-cebf5-firebase-adminsdk-tkvzz-370d162330.json')
        default_app = firebase_admin.initialize_app(cred)
    actual=[]
    to_pred=[]
    your_list=[]
    absent=[]
    rolls=[]
    emails=[]
    alls=[]
    db = firestore.client()
    userref=db.collection(u"Attendance").document(u"CSE A").collection(u"09-Jul-2019")
    allstud=db.collection(u"Students")
    stud_count=userref.stream()
    i=0
    ass=allstud.stream()
    for d in ass:
        print(d.to_dict().get("REG"))
        alls.append(d.to_dict().get("REG"))
        emails.append(d.to_dict().get("EM"))
    for doc in stud_count:
        i=i+1
        # print(u'{} => {}'.format(doc.id, doc.to_dict().get("UID")))
        time= doc.to_dict().get("UID")[11:]
        print("\n"+time)
        actual.append(time[3:5])
        to_pred.append(doc.to_dict().get("BUS"))
        rolls.append(doc.to_dict().get("ROLL"))
    
    print(rolls)
    print("itc isssz")
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
        if(val>15):
            print("REJECTED")
            your_list.append((rolls[i]))
        i=i+1
    for j in rolls:
        if(j not in alls):
            absent.append(j)
    print(absent)
    x=0
   
    
    
    return render_template('index.html', your_list=your_list)
    
@app.route('/')
def hello():
    
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
