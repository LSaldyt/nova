from gtts import gTTS
import os

def speak(audioString):
    tts = gTTS(text=audioString, lang='en')
    tts.save('.audio.mp3')
    os.system('mpg321 .audio.mp3')
