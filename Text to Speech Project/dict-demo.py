from tkinter import *
from tkinter import ttk

language = {"English":"en",
            "Hindi":"hi",
            "French":"fr",
            "Spanish":"es"}

def output():
     lang = (language_combo.get())
     print(language[lang])



window =Tk()
window.geometry("400x400")

language_combo = ttk.Combobox(window,
                              values=["English","Hindi","French","Spanish"],
                              )
language_combo.pack()
language_combo.set('English')

btn = Button(window,
             command = output,
             text = "submit")
btn.pack(pady="30")


# Create a Text widget and set default text
text_widget = Text(window, height=5, width=30)

text_widget.insert('1.0',"write")
text_widget.pack()



window.mainloop()