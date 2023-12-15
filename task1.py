"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""


import tkinter as tk
from tkinter import *

win = tk.Tk()
win.geometry("600x200")




l1 = Label(win,text="name:")
l2 = Label(win,text="student number:")
l3 = Label(win,text="grade:")
e1 = Entry(win,width=20)
e2 = Entry(win,width=20)
e3 = Entry(win,width=20)
b1 = Button(win,text="Click to return information to database")




def clickFunction(event):
    print(event)
    name = e1.get()
    name = str(name)
    stnum = e2.get()
    stnum = float(stnum)
    grade = e3.get()
    grade = float(grade)
    print(name, stnum,grade)
b1.bind("<Button>",clickFunction)

l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
l2.grid(row=1,column=3)
e2.grid(row=1,column=4)
l3.grid(row=1,column=5)
e3.grid(row=1,column=6)
b1.grid(row=2,column=1,columnspan=6)



win.mainloop()
