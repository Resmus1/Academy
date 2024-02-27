# Введение в tkinter. Главное окно

import tkinter as tk

win = tk.Tk()
h = 500
w = 600
icon = tk.PhotoImage(file='../Projects/img/test.png')
win.iconphoto(False, icon)
win.config(bg='#CD853F')
win.title('Тестируем Ткинтер')
win.geometry(f"{h}x{w}+100+200")
win.minsize(300, 400)
win.maxsize(700, 800)
win.resizable(True, True)
win.mainloop()
