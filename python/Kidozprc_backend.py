import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from gtts import gTTS
import os

import urllib.request
import time

old = ''
print("Open Program!")

def connect(host='https://kidozprc2021-default-rtdb.firebaseio.com/'):
    
    Internet = False
    while Internet == False:
        try:
            urllib.request.urlopen(host)
            Internet = True

        except:
            Internet = False
            print("No Internet in connect")
            time.sleep(0.5)
        else:
            print("Connected!")


def stream_handler():
    global old
    Date = db.reference("Date").get()
    if old != Date:
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
        old = db.reference("Date").get()
    else:
        pass


connect()

try:
    cred = credentials.Certificate("kidozprc2021.json")
    firebase_admin.initialize_app(cred,{'databaseURL':'https://kidozprc2021-default-rtdb.firebaseio.com/'})
    old = db.reference("Date").get()
except FileNotFoundError:
    print("Please put kidozprc2021.json in the same directory!")
    time.sleep(3)
    quit()

while True:
    try:
        stream_handler()
    except firebase_admin.exceptions.UnavailableError:
        connect()
    except urllib.error.URLError:
        connect()
    except:
        pass

