import tkinter as tk
import winsound
import os, sys
from tkinter import *
from tkinter import filedialog,simpledialog
from tkinter import messagebox
from tkinter.ttk import *
import tkinter.messagebox
import re


def doNothing():
    print("OK I won't reset anything")



class Application(tk.Frame):


    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.running = False
        self.time = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.build_interface()

    def build_interface(self):

        self.time_entry = tk.Entry(self)
        self.time_entry.grid(row=0, column=1, ipadx=25, ipady=15)
        '''
        EntryList = []
        for i in range(81):
            EntryList.append(tk.Entry(root, font=("Calibri", 12), justify="center", width=6, bg="#1E6FBA", fg="yellow",
                                   disabledbackground="#1E6FBA", disabledforeground="yellow",
                                   highlightbackground="black", highlightcolor="red", highlightthickness=1, bd=0))
            EntryList[i].grid(row=i / 9, column=i % 9, ipady=14)
        '''
        self.clock = tk.Label(self, text="00:00:00\n", font=("consolas", 20), width=10)
        self.clock.grid(row=1, column=1, stick="S")

        self.time_label = tk.Label(self, text="hour:: min ::sec\n", font=("consolas", 10), width=20)
        self.time_label.grid(row=2, column=1, sticky="N")

        self.power_button = tk.Button(self, text="Start", bg="blue",activebackground="green",command=lambda: self.start())
        self.power_button.grid(row=3, column=0, sticky="NE", ipadx=11, ipady=11, padx=10)

        self.reset_button = tk.Button(self, text="Reset", bg="blue",  activebackground = "red", command=lambda: self.reset())
        self.reset_button.grid(row=3, column=1, sticky="NW", ipadx=11, ipady=11)

        #self.labelText = tk.Label(root, text="codin-studios Corp.").pack(sticky=S)
        self.quit_button = tk.Button(self, text="Quit", bg="yellow", fg="blue", highlightbackground = "red",  activebackground = "red", activeforeground="blue",command=lambda: self.quit())
        self.quit_button.grid(row=3, column=3, sticky="NE", ipadx=11, ipady=11)

        self.master.bind("<Return>", lambda x: self.start())
        self.time_entry.bind("<Key>", lambda v: self.update())

    def calculate(self):
        #Calculates the time
        self.hours = self.time // 3600
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    def update(self):

        self.time = int(self.time_entry.get())
        try:
            winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
            self.clock.configure(text=self.calculate())
        except:

            self.clock.configure(text="00:00:00")

    def timer(self):

        if self.running:
            if self.time <= 0:
                winsound.PlaySound("mario_dies.wav", winsound.SND_ASYNC)
                self.clock.configure(text="Time's up!")
            else:
                self.clock.configure(text=self.calculate())
                self.time -= 1
                self.after(1000, self.timer)

    def start(self):
        try:
            winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
            self.time = int(self.time_entry.get())
            self.time_entry.delete(0, 'end')
        except:
            self.time = self.time
        self.power_button.configure(text="Stop", command=lambda: self.stop())
        self.master.bind("<Return>", lambda x: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False
        self.time = 0
        self.clock["text"] = "00:00:00"

        answer = tkinter.messagebox.askquestion("Exit ", "Are you sure that yo wanna reset this shit?")
        if answer == "yes":
            root.build_interface()
        else:
            doNothing()


    def quit(self):
        if tk.messagebox.askokcancel("Quit", "Do you wanna quit?"):
            root.destroy()

    def about(self):
        label = messagebox.showinfo("About", "This is a GUI python Timer which can be used to set timer for a specific time")



if __name__ == "__main__":
    root = tk.Tk()
    root.title("TIMER")
    root.configure(background='black')
    root.geometry("310x250")
    root.resizable(width=False, height=False)
    Application(root).pack(side="top", fill="both", expand=True)

    MainMenu = Menu(root)
    root.config(menu=MainMenu)

    mainFile = Menu(MainMenu)
    MainMenu.add_cascade(label='File', menu=mainFile)
    mainFile.add_separator()
    mainFile.add_command(label='Exit', command=quit)

    about = Menu(MainMenu)
    MainMenu.add_cascade(label='About', menu=about)
    about.add_command(label='About', command=about)

    t = 0

    def set_timer(self):
        global t
        t = t + int(e1.get())
        return t


    times = StringVar()
    e1 = Entry(root, textvariable=times)
    e1.pack()
    b1 = Button(root, text="SET", width=20, command=set_timer)
    b1.pack()
    root.mainloop()