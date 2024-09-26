#tkinter is used to create Graphical User Interface 
import tkinter as tk
#time module is used to manipulate the time
from time import strftime

root = tk.Tk()
#title of the root is set as Digital clock 
root.title("Digital clock")

#function to define the time inside root 
def time():
    string = strftime("%H:%M:%S %p \n %D")
    label.config(text=string)
    label.after(1000,time)

#set the font background and foreground color of the root
label = tk.Label(root,font=('times new roman',50,'bold'),background="#ac9362",foreground="#341c02")
label.pack(anchor='center')

time()
root.mainloop()