import pygame
from tkinter import *
import winsound
'''
pygame.init()
deathSound = pygame.mixer.Sound('mario_dies.wav')
startingSound = pygame.mixer.Sound('laser.wav')
'''
t = 0
def set_timer():
    global t
    t = t+int(e1.get())
    return t
def countdown():
    global t
    if t>0:
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        #startingSound.play()
        l1.config(text=t)
        t=t-1
        l1.after(1000, countdown)
    elif t==0:
        winsound.PlaySound("mario_dies.wav", winsound.SND_ASYNC)
        #deathSound.play()
        print("END")
        l1.config(text="You're UP")



root = Tk()
root.geometry("200x200")
root.resizable(width=False, height=False)
root.title("Timer")

l1 = Label(root, font="times 20")
l1.grid(row=1, column=2)

times = StringVar()
e1 = Entry(root, textvariable=times)
e1.grid(row=3, column=2)

b1 = Button(root, text="SET", width=20, command=set_timer)
b1.grid(row=4, column=2, padx=20)

b2 = Button(root, text="START", width=20, command=countdown)
b2.grid(row=6, column=2, padx=20)


root.mainloop()
#pygame.display.update()