import sys
import random
import datetime
import webbrowser
import wikipedia
import pyowm
import ipinfo
import requests
from gtts import gTTS as gtts
from playsound import playsound
import os
from subprocess import Popen

access_token='1b3c9e5e3dca7a'
owm=pyowm.OWM("d09e5ef276efa2a6957ff7cefe29c42e")

#DATABASE
greetings = ['hey there', 'hello', 'hi', 'hai', 'hey!', 'hey']
question = ['how are you?', 'how are you doing?']
responses = ['i\'m Okay', "i\'m fine","i am doing good"]
var1 = ['who made you', 'who created you']
var2 = ['i was created by gray hat right in his computer.', 'gray hat', 'some guy whom i never got to know. called himself grayhat']
var3 = ['what time is it', 'what is the time', 'time' , 'tell me the date and time' , 'time right now' , 'today\'s date']
var4 = ['who are you', 'what is you name','what\'s your name','what should i call you']
cmd1 = ['open browser', 'open google']
cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn\'t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd4 = ['open youtube', 'i want to watch a video']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
cmd8 = ['what is you favourite colour', 'which is your favourite color']
cmd9 = ['thank you']
repfr9 = ['youre welcome', 'glad i could help you']
#DATABASE ENDS

def doProcess(score=[]):
    mAx=max(score)
    if mAx==score[0]:
        random_greeting = random.choice(greetings)
        Popen("python play.py 1 "+random_greeting,shell=False)
    elif mAx==score[1] :
        random_reply = random.choice(responses)
        Popen("python play.py 1 "+random_reply,shell=False)
    elif mAx==score[2] :
        random_reply = random.choice(var2)
        Popen("python play.py 1 "+random_reply,shell=False)
    elif mAx==score[3] :
        random_reply = random.choice(repfr9)
        Popen("python play.py 1 "+random_reply,shell=False)
    elif mAx==score[4] or mAx==score[5]:
        random_reply = random.choice(colrep)
        Popen("python play.py 1 "+random_reply,shell=False)
    elif mAx==score[6] :
        #playSongs()
        print("PLAY SONGS")
    elif mAx==score[7] :
        random_reply="I am Gray Bot. Your Personal Music Assistant"
        Popen("python play.py 1 "+random_reply,shell=False)
    elif mAx==score[8] :
        print("RUN YT")
    elif mAx==score[9] :
        random_reply="Bye. Hope to talk to you soon again"
        Popen("python play.py 1 "+random_reply,shell=False)
        sys.exit(0)
        return
    elif mAx==score[10] :
        handler=ipinfo.getHandler(access_token=access_token)
        ip_address=requests.get('https://api.ipify.org/?format=json').json()['ip']
        details=handler.getDetails(ip_address=ip_address)
        print(details.all)
        LAT = float(""+str(details.latitude))
        LON = float(""+str(details.longitude))
        observation=owm.weather_at_coords(lat=LAT,lon=LON)
        w=observation.get_weather()
        random_reply0="Wind Speed "+str(w.get_wind().get("speed"))+"metre per second"
        random_reply1="Humidity " + str(w.get_humidity())+" percentage"
        random_reply2="Temperature " + str(w.get_temperature('celsius').get('temp'))+" degree celsius"
        fnalreply=random_reply0+" "+random_reply1+" "+random_reply2
        Popen("python play.py 0 "+fnalreply,shell=False)
    elif mAx==score[11] :
        random_reply0="Today's Date : "+str(datetime.date.today())
        time=str(datetime.datetime.now().time()).split(":")
        random_reply1="Current Time : "+time[0]+" "+time[1]
        fnalreply=random_reply0+" "+random_reply1
        Popen("python play.py 0 "+fnalreply,shell=False)
    elif mAx==score[12]:
        random_reply="Opening Browser"
        Popen("python play.py 1 "+random_reply,shell=False)
        webbrowser.open('www.google.com')
    elif mAx==score[13]:
        response=random.choice(jokes)
        random_reply="Here's a Joke for you : \n"+response
        Popen("python play.py 1 "+random_reply,shell=False)
        

def execute(content=""):
    cont=content.lower().split(" ")
    print(cont)
    score=[0 for i in range(14)]
    for con in cont:
        for greet in greetings:
            grt=greet.split(' ')
            if con in grt:
                score[0]+=1
        for greet in question:
            grt=greet.split(' ')
            if con in grt:
                score[1]+=1
        for greet in var1:
            grt=greet.split(' ')
            if con in grt:
                score[2]+=1
        for greet in cmd9:
            grt=greet.split(' ')
            if con in grt:
                score[3]+=1
        for greet in cmd7:
            grt=greet.split(' ')
            if con in grt:
                score[4]+=1
        for greet in cmd8:
            grt=greet.split(' ')
            if con in grt:
                score[5]+=1
        for greet in cmd2:
            grt=greet.split(' ')
            if con in grt:
                score[6]+=1
        for greet in var4:
            grt=greet.split(' ')
            if con in grt:
                score[7]+=1
        for greet in cmd4:
            grt=greet.split(' ')
            if con in grt:
                score[8]+=1
        for greet in cmd6:
            grt=greet.split(' ')
            if con in grt:
                score[9]+=1
        for greet in cmd5:
            grt=greet.split(' ')
            if con in grt:
                score[10]+=1
        for greet in var3:
            grt=greet.split(' ')
            if con in grt:
                score[11]+=1
        for greet in cmd1:
            grt=greet.split(' ')
            if con in grt:
                score[12]+=1
        for greet in cmd3:
            grt=greet.split(' ')
            if con in grt:
                score[13]+=1
    doProcess(score)
        
    

if __name__ == "__main__":
    inp=sys.argv[1:]
    inpt=""
    for arg in inp:
        inpt+=arg+" "
    inpt=inpt.strip()
    execute(inpt)