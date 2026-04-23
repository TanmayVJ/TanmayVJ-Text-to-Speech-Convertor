import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import ttk
import pyttsx3
from gtts import gTTS
from playsound import playsound
import os

window = Tk()
window.title("Text to Speech")
window.geometry("900x450+200+200")
window.resizable(False,False)
window.config(bg= "#305065")

engine = pyttsx3.init()

# all language accents (from New.py)
language = {"English":"en",
            "Hindi":"hi",
            "French":"fr",
            "Spanish":"es"}

def speaknow():
    text = text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    language_choose = language_combobox.get()
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

    # If a non-English accent is selected, use gTTS for that language
    if language_choose != "English":
        bhasha = language.get(language_choose)
        output = gTTS(text=text, lang=bhasha)
        filename = "audio.mp3"
        output.save(filename)
        playsound(filename)
        os.remove(filename)
    else:
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
    language_choose = language_combobox.get()
    voices = engine.getProperty('voices')

    # If a non-English accent is selected, use gTTS for that language
    if language_choose != "English":
        bhasha = language.get(language_choose)
        output = gTTS(text=text, lang=bhasha)
        filename = "audio.mp3"
        output.save(filename)
        src = os.path.abspath(filename)
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("audio files", "*.mp3"),("text files", "*.txt*"), ("All files", "*.*")])
        if file_path:
            os.rename(src, file_path)
        else:
            os.remove(src)
    else:
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

### language/accent (from New.py) ###

Label(window,
      text="ACCENT" ,font="arial 15 bold",
      bg = "#305065", fg= "white").place(x = 645,
                                         y = 240)

language_combobox = ttk.Combobox(window,
                           values = ['English','Hindi','French','Spanish'],
                           font = ("Arial", 14),
                           width= 10,
                          )
language_combobox.place(x = 620,
                     y = 275)
language_combobox.set('English')

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
btn.place(x= 550, y = 330)

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
save.place(x= 730, y = 330)



window.mainloop()
