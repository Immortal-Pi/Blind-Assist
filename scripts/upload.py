import requests
import cv2
import os
from time import sleep
import ast

def send():
        #item = raw_input()
        capture = cv2.VideoCapture(0)
        ret, frame = capture.read()
        cv2.imwrite("image.jpg",frame)
        if ret:
            url = "http://10.0.4.204:8000/BlindAssist/FindObject/"
            f = open('image.jpg','rb')
            r = requests.post(url,files={'image':f},data={'obj':'scene'})
            #print(r.status_code)
            if r.status_code == 200:
                sleep(3)
                result = requests.post("http://10.0.4.204:8000/BlindAssist/result/")
                print(type(result.text))
        capture.release()
        return ast.literal_eval(result.text)
#print(type(send()))


