import speech_recognition as sr 
from gtts import gTTS as gtts
from playsound import playsound
import os
from subprocess import Popen

language='en-IN'

#Sample rate is how often values are recorded 
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) here. 
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
#Initialize the recognizer 
r = sr.Recognizer() 


with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
    #wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source)
    while True:
      #os.system("python play.py "+"Say Something")
      Popen("python play.py "+"0 0",shell=False).wait()
      print("Say Something")
      #listens for the user's input
      audio = r.listen(source,timeout=1)
      print("Processing..")
      try:
          text = r.recognize_google(audio,language=language)
          #print("TEXT\n",str(text))
          os.system("python commands.py "+text)
          #performOp(text)
      except sr.UnknownValueError:
        print("Gray Speech Recognition could not understand audio")
        Popen("python play.py "+"0 1",shell=False)
      except sr.RequestError as e:
          print("Could not request results from Gray Speech Recognition service; {0}".format(e))
          Popen("python play.py "+"0 2",shell=False)
      break