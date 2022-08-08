#!/bin/python3
#code=_-udf:8-_
#creater : 

import os,sys
import time
from gtts import gTTS
import string,random 

# 01 : Create Def Wtite Text -->
def type_text(text,timex): # DONE
    for e in text + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(timex)

# 02 : Create Def Create Mp3 File -->
def play_audio(file,text): #DONE
    my_text = gTTS(text)
    my_text.save(file)


# 03 : Create def play audio file -->
def play_audio(file): #DONE
    try:
        os.system(f"play-audio {file}")
    except Exception as e:
        print(e)

# Create Def fb new auto_random uid dump --
def random_new_dump(): # DONE
    os.system("clear")
    try:
        user = []
        print("[*] Enter First 6 digit of any UID")
        print("[*] 100000   100010  100020")
        print("[*] 100083   100084  100085")
        user_id = input("[*] Enter Digit User ID : ")
        save_file = input("[*] Dump File Save As : ")
        if len(user_id)==6:
            code = user_id
        elif len(user_id)>6:
            code = user_id[:6]
        else:
            print("Wrong User Input")
            exit()
        limit = int(input("[*] Enter Dump Limit : "))
        if (limit)>5000:
            limit = 5000
        for number in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(9))
            user.append(nmp)
        dumpp = open(save_file,'w')
        for bilal in user:
            uid = code+bilal
            dumpp.write(uid+'\n')
            print(uid)
            time.sleep(0.05)
        dumpp.close()
        print("Dumping Done ")
        print(f"Your File Save As {save_file}")
    except Exception as e:
        print(e)

def random_old_dump(): # DONE
    os.system("clear")
    try:
        user = []
        print("[*] Enter First 6 digit of any UID")
        print("[*] 1000000   10000000  100000000")
        #print("[*] 100083   100084  100085")
        user_id = input("[*] Enter Digit User ID : ")
        save_file = input("[*] Dump File Save As : ")
        if len(user_id)==6:
            digitt = 9
        elif len(user_id)==7:
            digitt = 8
        elif len(user_id)==8:
            digitt = 7
        elif len(user_id)==9:
            digit = 6
        else:
            print("Wrong User Input")
            exit()
        code = user_id
        limit = int(input("[*] Enter Dump Limit : "))
        if (limit)>5000:
            limit = 5000
        for number in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(digitt))
            user.append(nmp)
        dumpp = open(save_file,'w')
        for bilal in user:
            uid = code+bilal
            dumpp.write(uid+'\n')
            print(uid)
            time.sleep(0.05)
        dumpp.close()
        print("Dumping Done ")
        print(f"Your File Save As {save_file}")
    except Exception as e:
        print(e)
