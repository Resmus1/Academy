# Знакомство с виджетами. Виджет Button
import tkinter as tk


def say_hello():
    print('Hello!')


def add_label():
    label = tk.Label(win, text='new')
    label.pack()

def counter():
    global count
    count += 1
    btn4['text'] = f"Счетчик {count}"


count = 0

win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title("Графическое Приложение")

btn1 = tk.Button(win, text='Hello',
                 command=say_hello,
                 )

btn2 = tk.Button(win, text='Add new label',
                 command=add_label,
                 )

btn3 = tk.Button(win, text='Add new label lambda',
                 command=lambda: tk.Label(win, text='new lambda').pack(),
                 )

btn4 = tk.Button(win, text=f"Счетчик {count}",
                 command=counter,
                 activebackground='blue',
                 bg='red',
                 state=tk.NORMAL,
                 )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

win.mainloop()
