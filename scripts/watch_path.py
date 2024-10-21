import cv2
import os
import ast
from heck import GuidePath

def send():
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    if ret:
        GuidePath(frame)
    capture.release()
    
if __name__=='__main__':
    while True:
        val = send()