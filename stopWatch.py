import tkinter as Tkinter
from tkinter import *
import tkinter as tk

counter = -1
running = False
def counter_label(label):
	def count():
		if running:
			global counter

			if counter==-1:
				display="Starting..."
			else:
				display=str(counter)

			label['text']=display
			label.after(1000, count)
			counter += 1

	count()

# ----------------- starting stopWatch -----------------------------------------
def Start(label):
	global running
	running=True
	counter_label(label)
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

# Stop function of the stopwatch
def Stop():
	global running
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False

# Reset function of the stopwatch
def Reset(label):
	global counter
	counter=-1

	# If reset is pressed after pressing stop.
	if running==False:
		reset['state']='disabled'
		label['text']='Wassup'

	# If reset is pressed while the stopwatch is running.
	else:
		label['text']='Starting...'

root = Tk()
root.title("Stopwatch")
root.geometry("100x150")
root.resizable(width=False, height=False)


root.minsize(width=400, height=100)
label = Tkinter.Label(root, text="Wassup", fg="black", font="consolas 30 bold")
label.pack()
start = Tkinter.Button(root, text='Start', width=15, command=lambda:Start(label))
stop = Tkinter.Button(root, text='Stop', width=15, command=Stop)
reset = Tkinter.Button(root, text='Reset', width=15, state='disabled', command=lambda:Reset(label))
start.pack()
stop.pack()
reset.pack()

root.mainloop()
