import tkinter as tk
from tkinter import ttk
import speech_recognition as sr 
from playsound import playsound
import AppOpener as ap
import pyttsx3 as p
import calendar as cd
import webbrowser as wb
import pywhatkit as py
from sketchpy import library as l
from datetime import date as d
import datetime as dt
import time as ti
dis = tk.Tk()
dis.minsize(1000,1000)
x = p.init('sapi5')
voices = x.getProperty('voices')
x.setProperty('voice',voices[3].id)
x.setProperty('rate',160)
ab = sr.Recognizer()
def voice(audio):
    lab=tk.Label(dis,text=f'ALEX : {audio}')
    lab.pack()
    x.say(audio)
    x.runAndWait()
def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        voice("Good Morning Sir")

    elif hour>=12 and hour<18:
        voice("Good Afternoon Sir")

    if hour>=18 and hour<20:
        voice("Good Evening Sir")

    elif hour>=20 and hour<0:
        voice("Good Night Sir")
    voice('HI ,I AM ALEX, how can i assist you ')
def AI():
    with sr.Microphone() as source:
        ab.pause_threshold = 0.8
        sk = ab.listen(source)
        try:
            voice("Recognizing you........")
            query = ab.recognize_google(sk, language='en-in')
            query = query.lower()
        except Exception as e:
            voice("I can't listen you")
            voice("say that again please")
            return ''
        return query
k = d.today()
b = k.year
t = ti.localtime()
a = ti.strftime("%I:%M %p", t)
def alex():
    wishMe()
    while True:
        y = AI()
        if "draw apj" in y:
            j=l.apj()
            j.draw()
            continue
        elif "hello" in y:
            voice('hello sir how can i assist you ? ')
            continue
        elif "search" in y :
            voice("What do you want to search.")
            inp = AI()
            py.search()
            continue
        elif 'play music' in y:
            playsound('D:/Saksham/python codes/alex/app.mp3')
            voice('want to talk more')
            continue
        elif 'calendar' in y:
            lab3=tk.Label(dis,text=cd.calendar(b,1,1,1))
            lab3.pack()
            continue
        elif 'draw rdj' in y:
            c = l.rdj()
            c.draw()
            continue
        elif 'game' in y:
            wb.open("https://poki.com/en/g/getaway-shootout")
            voice("Let's Play")
            continue
        elif 'time' in y:
            voice(a)
            continue
        elif 'your name' in y:
            voice("MY NAME IS ALEX")
            continue
        elif 'open youtube' in y:
            wb.open("https://www.youtube.com")
            continue
        elif 'open google' in y:
            wb.open("https://www.google.com")
            continue
        elif 'open wikipedia' in y:
            wb.open("https://www.wikipedia.org")
            continue
        elif 'open calculator' in y:
            ap.open('Calculator')
            continue
        elif 'open whatsapp' in y:
            ap.open('WhatsApp')
            continue
        elif 'close calculator' in y:
            ap.close('Calculator')
            continue
        elif 'close whatsapp' in y:
            ap.close('WhatsApp')
            continue
        elif 'open zoom' in y:
            ap.open('Zoom')
            continue
        elif 'close zoom' in y:
            ap.close('Zoom')
            continue
        elif 'by' in y:
            voice("ok then, talk to you soon")
            break
        else :
            x.say("I Dont Have More Commands To Say")
            x.runAndWait()
            x.say("Please say anything else")
            x.runAndWait()
            continue
    voice("This is our conversation")
    voice('thanks for talking with me')
btn = ttk.Button(dis,text='Start', command=alex)
btn.pack()
dis.mainloop()
