from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import ttk
import gtts
from gtts import gTTS
import os
from playsound import playsound 

    
    #gender = gender_combobox.get()
    #speed = speed_combobox.get()
    #voices = engine.getProperty('voices')
    
language = {"English":"en",
            "Hindi":"hi",
            "French":"fr",
            "Spanish":"es"}

#engine = pyttsx3.init()

def speaknow():
    global language
    language_choose = language_combobox.get()
    bhasha = (language.get(language_choose))
    text_info = text_area.get(1.0, END)
    #language = lang
    output = gTTS(text= text_info,lang= bhasha )
    #engine.say(output)
    #engine.runAndWait()
    filename = "audio.mp3"
    output.save(filename)
    playsound(filename)
    os.remove(filename)
    #del(filename)

#def common():
 #   global language
  #  language_choose = language_combobox.get()
   # lang = (language[language_choose])
    #print("You have selected "+lang +".")


def download():
    global language
    language_choose = language_combobox.get()
    bhasha = (language.get(language_choose))
    text_info = text_area.get(1.0, END)
    #language = lang
    output = gTTS(text= text_info, lang = bhasha)
    filename = "audio.mp3"
    output.save(filename)
    #global loc
    #os.getcwd(filename)
    #os.getcwd()
    src = os.path.abspath(filename)
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("audio files", "*.mp3"),("text files", "*.txt*"), ("All files", "*.*")])
    #os.chdir(file_path)
    os.rename(src,file_path)
    os.remove(filename)
    
# main GUI

window = Tk()
window.title("Text to Speech")
window.geometry("900x450+200+200")
window.resizable(False,False)
window.config(bg= "#305065")


#icon
icon = PhotoImage(file="text icon.png")
window.iconphoto(False, icon)

#top frame
top_frame = Frame(window, bg="orange", width = 900,height = 100)
top_frame.pack(side = "top")

img = Image.open("mic logo.png")
#img = Image.open("text icon.png")
resized = img.resize((150,100))
logo = ImageTk.PhotoImage(resized)

Label(top_frame, image= logo,bg="orange").place(x = 2,
                                                y = 2)
Label(top_frame, 
      text="TEXT TO SPEECH CONVERTOR",
      font = "arial 30 bold",
      bg="orange",
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
                 bg="white", fg="black",
                relief= GROOVE,
                 wrap="word" )
text_area.place(x = 135,y = 120, width=600,height= 200)


Label(window,
      text="LANGUAGE" ,font="arial 15 bold",
      bg = "#305065", fg= "white").place(x = 750,
                                         y = 160)

language_combobox = ttk.Combobox(window,
                           values = ['English','Hindi','French','Spanish'],
                           font = ("Arial", 14),
                           width= 10,
                          )
language_combobox.place(x = 750, 
                     y = 200)
language_combobox.set('English')

speak = Image.open("speak.png")
speak_resized = speak.resize((50,50))

speak_img = ImageTk.PhotoImage(speak_resized)

btn = Button(window,
             text = "Speak", font= "arial 13 bold",
             width = 120,
             image= speak_img,
             compound="left",
             command= speaknow,
             bg = "white")
btn.place(x= 280, y = 350)

## download section  ##

download_img = Image.open("download.png")
download_resized = download_img.resize((50,50))

save_img = ImageTk.PhotoImage(download_resized)

save = Button(window,
             text = "Save", font= "arial 13 bold",
             width = 120,
             image= save_img,
             command= download,
             compound= LEFT
             )
save.place(x= 500, y = 350)




window.mainloop()