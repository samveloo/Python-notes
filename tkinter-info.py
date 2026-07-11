from tkinter import *

def hello(event):
    print("Привет, программист!")

root = Tk() # создаем переменную
root.title("Заголовок окна программы") #заголовок окна
root.geometry("400x200") # начальные размеры окна

but1 = Button(root)
but1["text"] = "Название кнопки"
but1.bind("<Button-1>", hello)
but1["text"] = "Нажми на меня!"
but1["width"] = 20
but1.pack()

input()