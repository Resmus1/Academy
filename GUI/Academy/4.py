# Как размещать виджеты при помощи метода grid

import tkinter as tk

win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title("Мое графическое приложение")

for i in range(5):
    for j in range(2):
        tk.Button(win, text=f"Hello {i} {j}").grid(row=i, column=j, sticky='we')
# btn1 = tk.Button(win, text='Hello1')
# btn2 = tk.Button(win, text='Hello2')
# btn3 = tk.Button(win, text='Hello3')
# btn4 = tk.Button(win, text='Hello world')
# btn5 = tk.Button(win, text='Hello5')
# btn6 = tk.Button(win, text='Hello6')
# btn7 = tk.Button(win, text='Hello7')
# btn8 = tk.Button(win, text='Hello8')
#
# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1, sticky='w')
# btn3.grid(row=1, column=0)
# btn4.grid(row=1, column=1)
# btn5.grid(row=2, column=0)
# btn6.grid(row=2, column=1, sticky='e')
# btn7.grid(row=3, column=0, columnspan=2, sticky='we')
# btn8.grid(row=0, column=2, rowspan=4, stick='ns')

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=150)

win.mainloop()
