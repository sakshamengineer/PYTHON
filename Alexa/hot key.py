import speech_recognition as sr
import pyttsx3 as pt
import os
ab = sr.Recognizer()
x = pt.init()
x.setProperty('rate',120)
def voice(audio):
    print(f'ALEX : {audio}')
    x.say(audio)
    x.runAndWait()
voice('Listening you ..........')
def AI():
    with sr.Microphone() as source:
        print("Listening you........")
        ab.pause_threshold = 1.2
        sk = ab.listen(source)
        try:
            print("Recognizing you........")
            query = ab.recognize_google(sk, language='en-in')
            query = query.lower()
            print(f"YOU SAID: {query}\n")
        except Exception as e:
            print("I can't listen you")
            print("please say it again")
            return ''
        return query
while True:
    y = AI() 
    if 'wake up alex' in y:
        os.startfile('D:\\Saksham\\alex2.py')
    elif 'turn off alex' in y:
        break
    