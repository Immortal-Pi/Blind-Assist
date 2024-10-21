import requests
import cv2
import os
from time import sleep
import ast

def send():
        #item = raw_input()
        capture = cv2.VideoCapture(0)
        ret, frame = capture.read()
        cv2.imwrite("lol.jpg",frame)
        if ret:
                url = "http://192.168.43.32:8000/BlindAssist/readText/"
                f = open('lol.jpg','rb')
                r = requests.post(url,files={'ocr_image':f})
                print(r.status_code)
                if r.status_code == 200:
                        sleep(3)
                        result = requests.post("http://192.168.43.32:8000/BlindAssist/speakText/")
                        print(type(result.text))
                print(ast.literal_eval(result.text))
                capture.release()
                return ast.literal_eval(result.text)

if __name__ == '__main__':
        send()

