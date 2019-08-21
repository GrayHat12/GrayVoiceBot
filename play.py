from gtts import gTTS as gtts
import sys
import os
from playsound import playsound

def execute(inpt="",sve=False):
    #print(inpt)
    if inpt=="0":
        playsound("./audio/say.mp3")
        return
    elif inpt=="1":
        playsound("./audio/error0.mp3")
        return
    elif inpt=="2":
        playsound("./audio/error1.mp3")
        return
    ninpt=inpt
    inpt=inpt.replace(" ","_")
    inpt=inpt.replace(".","_")
    inpt=inpt.replace("/","_")
    inpt=inpt.replace("\\","_")
    inpt=inpt.replace("|","_")
    inpt=inpt.replace(":","_")
    inpt=inpt.replace("*","_")
    inpt=inpt.replace("?","_")
    inpt=inpt.replace(">","_")
    inpt=inpt.replace("<","_")
    inpt=inpt.replace("\n","")
    inpt=inpt.replace("\t","")
    inpt=inpt.replace("\'","")
    inpt=inpt.replace(",","")
    inpt=inpt.replace(":","")
    if sve:
        if os.path.isfile('./audio/'+inpt+'.mp3'):
            playsound("./audio/"+inpt+".mp3")
            return
        else:
            gtts(text=ninpt,lang='en-IN',slow=False).save("./audio/"+inpt+".mp3")
            playsound("./audio/"+inpt+".mp3")
            return
    else:
        gtts(text=ninpt,lang='en-IN',slow=False).save("./audio/"+inpt+".mp3")
        playsound("./audio/"+inpt+".mp3")
        os.remove("./audio/"+inpt+".mp3")
        return

if __name__ == "__main__":
    inp=sys.argv[2:]
    inpt=""
    for arg in inp:
        inpt+=arg+" "
    inpt=inpt.strip()
    execute(inpt,bool(int(sys.argv[1])))