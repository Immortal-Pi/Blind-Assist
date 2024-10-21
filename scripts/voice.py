import speech_recognition as sr
from time import ctime
import time
import nltk as nk
import os
import path_upload
from gtts import gTTS
import upload
import ocr_upload
import cv2
#from take_photo import click

VALID_ALPHA='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
def speak(audio_string):
        print(audio_string)
        tts = gTTS(text=audio_string,lang='en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")

def recordAudio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                #print("Say something")
                audio = r.listen(source)
                data = ""
                try:
                        data = r.recognize_google(audio)
                        print(" Command:"+data)
                except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))

                return data

def wake_up(data):
        tokens = nk.word_tokenize(data)
        print(tokens)
        if "hello" or "are" and "you" and "there" in tokens:
                speak("Hi,how may i help you?")
                return True
        return False

def Assistant(data):
        tokens = nk.word_tokenize(data)
        print(tokens)
        if "where" and "bottle" in tokens:
                speak("I have found your bottle, it is on the table.")
        elif ("what" and "is" and  "this") or ("what" and "am" and "looking" and "at") or ("what" and "is" and "it" and "called") in tokens:
                things_found=''
                things = upload.send()
                print(things)
                for thing in things:
                        if float(things[thing]['confidence']) > 0.40:
                                things_found+=things[thing]['label']+', '
                speak("I think you are looking at a "+things_found)
        elif ("read" and "this") or "read" or "translate" in tokens:
                toSpeak = None
                tell = ''
                toSpeak = ocr_upload.send()
                for i in toSpeak.keys():
                        word = toSpeak[i]
                        if word.isalpha():
                                tell+=word+' '
                print(tell)
                try:
                        speak(tell)
                except:
                        speak("Sorry,Could not translate.")
        elif "guide" and "me" and "for" in tokens:
                for i in tokens:
                        if i.isdigit():
                                path_upload.guide_me(int(i))
                                break
        else:
                speak("Sorry could not understand")
    # os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
if __name__ == '__main__': 
        # initialization
        time.sleep(2)
        speak("Assistant Online")
        while True:
                data = recordAudio()
                #data = raw_input()
                if data == '':
                        pass
                if wake_up(data):
                        print("give command")
                        data = recordAudio()
                        Assistant(data) 
                print("Inro")
