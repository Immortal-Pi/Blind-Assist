import requests
import cv2
import os
from time import sleep
from gtts import gTTS
import ast
#capture = cv2.VideoCapture(0)
def send():
        #item = raw_input()
        capture = cv2.VideoCapture(0)
        ret, frame = capture.read()
        cv2.imwrite("lol.jpg",frame)
	if ret:
            return GuidePath(frame)
        capture.release()

if __name__ == '__main__':
##def guide_me(time=10):
	time=10
        cnt=0
        while True:
                val = send()
                if val=='None':
                        cnt+=1
                        print(val)
                else:
                        print(val,cnt)
                        tts = gTTS(text="Please move "+val,lang='en')
                        tts.save("dir.mp3")
                        os.system("mpg321 dir.mp3")
                sleep(0.25)
                if cnt == (time//0.25):
                        break
#       capture.release()

