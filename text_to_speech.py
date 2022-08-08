from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
import random

root = Tk()
root.geometry("500x500") 
root.configure(bg='ghost white')
root.title("TEXT TO SPEECH")

Label(root, text = "TEXT TO SPEECH", font = "arial 20 bold", bg='white').pack()
Label(text ="PROGRAM BY BHARATH", font = 'arial 15 bold', bg ='white' , width = '20').pack(side = 'bottom')
Label(root,text ="Enter Text", font = 'arial 15 bold').place(x=20,y=60)
Input_text = Text(root,font = 'arial 10', height = 14, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=20,y=100)

def Text_to_speech():
    Message = Input_text.get(1.0, END)
    speech = gTTS(text = Message)
    a=str(random.randint(1,101))
    file='text to speech'+a+'.mp3'
    speech.save(file)
    playsound(file)
    os.remove(file)

def Exit():
    root.destroy()

def reset():
    Input_text.delete(1.0, END)
Button(root, text = "PLAY", font = 'arial 18 bold' , command = Text_to_speech ,width = '5',bg='yellow').place(x=40,y=350)

Button(root, font = 'arial 18 bold',text = 'EXIT', width = '5' , command = Exit, bg = 'OrangeRed1').place(x=340 , y = 350)

Button(root, font = 'arial 18 bold',text = 'RESET', width = '6' , command = reset, bg = 'lightblue').place(x=180 , y = 350)

root.mainloop()
