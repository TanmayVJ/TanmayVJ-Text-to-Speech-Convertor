from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import ttk
from gtts import gTTS
import os
from playsound import playsound 

# all language , can be updated

language = {"English":"en",
            "Hindi":"hi",
            "French":"fr",
            "Spanish":"es"}

# to delete the > sign from text box

def on_key_release(event):
    global first_key_release
    if first_key_release:
        # Delete the inserted text
        text_area.delete("1.0")
        first_key_release = False
    
    

# function for speaking purpose

def speaknow():
    global language
    language_choose = language_combobox.get()
    bhasha = (language.get(language_choose))
    text_info = text_area.get("1.0", END)
    output = gTTS(text= text_info,lang= bhasha )
    filename = "audio.mp3"
    output.save(filename)
    playsound(filename)
    os.remove(filename)

# funtion for downloading

def download():
    global language
    language_choose = language_combobox.get()
    bhasha = (language.get(language_choose))
    text_info = text_area.get(1.0, END)
    output = gTTS(text= text_info, lang = bhasha)
    filename = "audio.mp3"
    output.save(filename)
    src = os.path.abspath(filename)
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("audio files", "*.mp3"),("text files", "*.txt*"), ("All files", "*.*")])
    os.rename(src,file_path)


#############    

# main GUI

window = Tk()

window.title("Text to Speech")
window.resizable(False,False)
window.geometry("1250x650")

#icon

icon = PhotoImage(file="text icon.png")
window.iconphoto(False, icon)

# window backgroung image

img = Image.open("design unnamed.png")
resized = img.resize((1250,650))
bg_image = ImageTk.PhotoImage(resized)

bg_image_label = Label(window,
                       image= bg_image)
bg_image_label.pack()


# text area to write 

first_key_release = TRUE

text_area = Text(window,
                 font="Robote 20",
                 bg="#ffffff", fg="black",
                relief= SOLID,
                 wrap="word", borderwidth= 0)
text_area.insert('1.0',">")
text_area.place(x = 204,y = 240, width=650,height= 390)
text_area.bind("<KeyRelease>", on_key_release)


# different language selection box

language_combobox = ttk.Combobox(window,
                           values = ['English','Hindi','French','Spanish'],
                           font = ("Arial", 14),
                           width= 10,
                          )
language_combobox.place(x = 1035, 
                     y = 242)
language_combobox.set('English')

# speak button

btn = Button(window,
             text = "Speak", font= "arial 14 bold",
             width = 6,
             height= 2,
             borderwidth= 0,
             command= speaknow,
             bg = "#227c9d",
             activebackground="#227c9d")
btn.place(x= 1070, y = 355)

# save button

save = Button(window,
             text = "Save", font= "arial 14 bold",
             width = 6,
             height= 2,
             bg= "#227c9d",
             activebackground="#227c9d",
             borderwidth= 0,
             command= download,
             )
save.place(x= 1062, y = 452)

credit = Label(text = "Made by TANMAY" , 
               bg = "black", fg = "white")
credit.place(x= 1000, y = 620)


window.mainloop()


############ PROJECT END ############