import tkinter as tk

win = tk.Tk()
win.geometry(f"600x300+100+200")
win.title("Генератор безопасных паролей")
icon = tk.PhotoImage(file='/GUI/Academy/img/password_icon.png')
win.iconphoto(False, icon)
win.config(bg='#CD853F')
win.resizable(False, False)

label = tk.Label(text="Генерируем пароль по следующим параметрам:",
                 bg='#CD853F',
                 fg='#B71C1C',
                 font=("Helvetica", 15, "bold"),
                 relief=tk.RIDGE,
                 bd=10,
                 )

num_checkbutton = tk.Checkbutton(text="Включать ли цифры?",
                                 bg='#CD853F',
                                 activebackground='#CD853F',
                                 highlightthickness=0,
                                 )
up_checkbutton = tk.Checkbutton(text="Включать ли прописные буквы?",
                                bg='#CD853F',
                                activebackground='#CD853F',
                                highlightthickness=0,
                                )
low_checkbutton = tk.Checkbutton(text="Включать ли строчные буквы?",
                                 bg='#CD853F',
                                 activebackground='#CD853F',
                                 highlightthickness=0,
                                 )
symbol_checkbutton = tk.Checkbutton(text="Включать ли символы?",
                                    bg='#CD853F',
                                    activebackground='#CD853F',
                                    highlightthickness=0,
                                    )
similar_checkbutton = tk.Checkbutton(text="Исключать ли неоднозначные символы?",
                                     bg='#CD853F',
                                     activebackground='#CD853F',
                                     highlightthickness=0,
                                     )

label.pack()
num_checkbutton.pack()
up_checkbutton.pack()
low_checkbutton.pack()
symbol_checkbutton.pack()
similar_checkbutton.pack()

win.mainloop()
