import speech_recognition as sr
import time
from subprocess import Popen
import winsound
import sys

frequency = 1500  # Set Frequency To 1500 Hertz
duration = 800  # Set Duration To 800 ms

sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
#stop_listening=None

# this is called from the background thread
def callback(recognizer, audio):
    print("Processing")
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        text=str(recognizer.recognize_google(audio,language="en-IN"))
        print(text)
        if text.lower().startswith("friday") or text.lower().startswith("riday"):
            winsound.Beep(frequency, duration)
            Popen("python commands.py "+text,shell=False).wait()
            winsound.Beep(frequency, duration)
            if text.lower().endswith("stop") or text.lower().endswith("quit"):
                print("STOPPED")
                winsound.Beep(frequency, duration)
                sys.exit(0)
        #print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
        return
    except sr.UnknownValueError:
        print("GRAY Speech Recognition could not understand audio")
        #Popen("python play.py "+"0 1",shell=False)
        return
    except sr.RequestError as e:
        print("Could not request results from GRAY Speech Recognition service; {0}".format(e))
        #Popen("python play.py "+"0 2",shell=False)
        return
    return
        
m = sr.Microphone(sample_rate=sample_rate,chunk_size=chunk_size)
print('MICROPHONE',m)

print(r.energy_threshold)
with m as source:
    r.adjust_for_ambient_noise(source)
    print(r.energy_threshold)
    
print("STARTED")
stop_listening=r.listen_in_background(m,callback)

time.sleep(10000)