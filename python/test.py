from firebase import firebase
import pyrebase
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
cred = credentials.Certificate('kidozprc2021-firebase-adminsdk-8ppdk-aaba88c937.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kidozprc2021-default-rtdb.firebaseio.com/'
})

firebase = firebase.FirebaseApplication('https://kidozprc2021-default-rtdb.firebaseio.com/', None)

def listener(event):
    print(event.data)  # new data at /reference/event.path. None if deleted

firebase_admin.db.child('ForWeb').listen(listener)