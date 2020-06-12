from threading import Thread
import speech_recognition as sr
from gtts import gTTS
import tkinter as tk    
import time

def inp():
    mystr=" "
    while True:
        print("a")

def runB():
    while True:
        print("b")

if __name__ == "__main__":
    t1 = Thread(target = runA)
    t2 = Thread(target = runB)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        pass