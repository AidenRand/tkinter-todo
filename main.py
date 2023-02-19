from tkinter import *
from tkinter import font

root = Tk()
root.geometry("500x500")

todos = []

inputFont = font.Font(size=22)
input = Entry(root, font=inputFont)
input.place(x=85, y=350)


taskBox = Listbox(root, width=70, height=20)
taskBox.pack(side="top")


class Task:
    def __init__(self, todo):
        self.todo = todo

    def printTodo(self):
        with open("todolist.txt", "a") as file:
            file.write(f"\n{self.todo}")
        todos.append(self.todo)
        taskBox.insert(END, self.todo)


def makeTodo():
    newTodo = Task(input.get())
    newTodo.printTodo()
    input.delete(0, END)


def openTaskFile():
    try:
        with open("todolist.txt", "r") as file:
            tasks = file.readlines()

        for task in tasks:
            if task != "/n":
                todos.append(task)
                taskBox.insert(END, task)
    except:
        file = open("todolist.txt", "w")
        file.close()


# Create buttons
btnFont = font.Font(size=16)

addTaskBtn = Button(root, font=btnFont, text="Add Task", width=10, command=makeTodo)
addTaskBtn.place(x=260, y=400)

delTaskBtn = Button(root, font=btnFont, text="Delete Task", width=10)
delTaskBtn.place(x=100, y=400)

root.mainloop()
