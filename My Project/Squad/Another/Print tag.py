import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from openpyxl import *


def open_file_surname():
    """
    Открывает активный лист, и возвращает список строк из него, преобразуя в список питон
    """
    global surname_list
    sheet = open_exel()
    for row in sheet.iter_rows(values_only=True):
        if row[0] is not None:
            surname_list.append(row[0])
    showinfo(title="Информация", message="Файл с Фамилиями загружен")


def open_exel():
    """
    Открывает файл ексель и получает активный лист
    """
    file_path = filedialog.askopenfilename()
    active_workbook = load_workbook(file_path)
    sheet = active_workbook.active
    return sheet



surname_list = []

win = tk.Tk()
win.geometry(f"400x200+100+200")
win.title("Создание бирок")
icon = tk.PhotoImage(file='img/tag.png')
win.iconphoto(False, icon)
win.resizable(False, False)







win.mainloop()