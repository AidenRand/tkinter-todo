from tkinter import *
from tkinter import messagebox
from tkinter import font

root = Tk()
root.geometry('500x500')

inputFont = font.Font(size=22)
input = Entry(root, font=inputFont)
input.place(x=85, y=350)

# Create buttons
btnFont = font.Font(size=16)

addTaskBtn = Button(root, font=btnFont, text='Add Task', width=10)
addTaskBtn.place(x=260, y=400)

delTaskBtn = Button(root, font=btnFont, text='Delete Task', width=10)
delTaskBtn.place(x=100, y=400)

# 

root.mainloop()