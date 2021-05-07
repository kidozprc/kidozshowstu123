import os
import time
from datetime import datetime
import urllib.request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from gtts import gTTS

cred = credentials.Certificate('kidoz2021.json')
firebase_admin.initialize_app(cred, {"databaseURL" : "https://kidozprc2021-default-rtdb.firebaseio.com/"})
Date = db.reference("Date").get()
veryold = db.reference("ForWeb").get()
new = veryold[str((Date)["Time"])]
now = time.asctime( time.localtime(time.time()))

print(Date["Time"])
roomspl = new["room"].split("/")
roomwithoutdot = roomspl[0].split(".")
room = "ออ" + roomwithoutdot[1] + "ทับ" + roomspl[1]
speak = new["name"] + " ห้อง " + room + "ผู้ปกครองมารับแล้วค่ะ"
language = 'th'


myobj = gTTS(text=speak, lang=language, slow= False)
myobj.save("arrive.mp3")
os.system("arrive.mp3")