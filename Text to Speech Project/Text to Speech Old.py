import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import ttk
import pyttsx3
import os

window = Tk()
window.title("Text to Speech")
window.geometry("900x450+200+200")
window.resizable(False,False)
window.config(bg= "#305065")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250) 
            setvoice()   
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60) 
            setvoice()           


def download():
    text = text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        
        else:
            engine.setProperty('voice',voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

    if(text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250) 
            setvoice()   
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60) 
            setvoice()           

#icon
icon = PhotoImage(file="text icon.png")
window.iconphoto(False, icon)

#top frame
top_frame = Frame(window, bg="white", width = 900,height = 100)
top_frame.pack(side = "top")

img = Image.open("mic logo.png")
#img = Image.open("text icon.png")
resized = img.resize((150,100))
logo = ImageTk.PhotoImage(resized)

Label(top_frame, image= logo,bg="white").place(x = 2,
                                                y = 2)
Label(top_frame, 
      text="TEXT TO SPEECH",
      font = "arial 30 bold",
      bg="white",
      fg= "black").place(x = 150,
                          y = 30)

###############

title = Label(window,
              text = "Write here : ",
              font= "Arial 15 bold")
title.place(x= 10,
            y = 120)


text_area = Text(window,
                 font="Robote 20",
                 bg="white", relief= GROOVE,
                 wrap=WORD)
text_area.place(x = 10,y = 160, width=500,height= 250)


### voice label ###
Label(window,
      text="VOICE" ,font="arial 15 bold",
      bg = "#305065", fg= "white").place(x = 580,
                                         y = 160)



gender_combobox = ttk.Combobox(window,
                           values = ['Male','Female'],
                           font = ("Arial", 14),
                           width= 10,
                           )
gender_combobox.place(x = 550,
                       y = 200)
gender_combobox.set('Male')

### speed level ###

Label(window,
      text="SPEED" ,font="arial 15 bold",
      bg = "#305065", fg= "white").place(x = 760,
                                         y = 160)

speed_combobox = ttk.Combobox(window,
                           values = ['Fast','Normal','Slow'],
                           font = ("Arial", 14),
                           width= 10,
                          )
speed_combobox.place(x = 730, 
                     y = 200)
speed_combobox.set('Normal')

## speak section ##

speak = Image.open("speak.png")
speak_resized = speak.resize((50,50))

speak_img = ImageTk.PhotoImage(speak_resized)

btn = Button(window,
             text = "Speak", font= "arial 13 bold",
             width = 120,
             image= speak_img,
             compound="left",
             command= speaknow
             )
btn.place(x= 550, y = 280)

## download section  ##

download_img = Image.open("download.png")
download_resized = download_img.resize((50,50))

save_img = ImageTk.PhotoImage(download_resized)

save = Button(window,
             text = "Save", font= "arial 13 bold",
             width = 120,
             image= save_img,
             compound="left",
             command= download
             )
save.place(x= 730, y = 280)



window.mainloop()