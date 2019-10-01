import os
import firebase_admin
import math
import requests 

from firebase_admin import credentials, storage
from firebase_admin import firestore
from firebase_admin.storage import bucket
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\Python-firebase\mark-me-cebf5-firebase-adminsdk-tkvzz-370d162330.json"
print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
if (not len(firebase_admin._apps)):
    cred = credentials.Certificate('D:\Python-firebase\mark-me-cebf5-firebase-adminsdk-tkvzz-370d162330.json')
    default_app = firebase_admin.initialize_app(cred,{'storageBucket':'mark-me-cebf5.appspot.com'})
bucket=storage.bucket()
print(bucket)
image_url = "https://firebasestorage.googleapis.com/v0/b/mark-me-cebf5.appspot.com/o/test_1.jpg?alt=media&token=d09edde1-fab9-4e91-9dfa-f3f461b0aaa8"
r=requests.get(image_url)
with open("a.jpg","wb") as f:
    f.write(r.content)
print("done")

os.system("conda activate opencv-env")
os.system("D:")
os.system("cd f")
os.system("python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7")