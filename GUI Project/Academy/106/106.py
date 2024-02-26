import tkinter as tk
from tkinter import filedialog
from openpyxl import *
from openpyxl.styles import Font, Alignment


def open_file_surnames():
    """
    Открывает текстовый файл и возвращает список строк из него.
    """
    global surname_list
    # Укажите путь к вашему файлу Excel
    file_path = filedialog.askopenfilename()
    # Открываем файл Excel
    workbook = load_workbook(file_path)
    # Получаем активный лист
    sheet = workbook.active
    # Проходимся по каждой строке и выводим значения ячеек в список
    for row in sheet.iter_rows(values_only=True):
        if row[0] is not None:
            surname_list.append(row[0])
    return surname_list


def generation_file_list():
    # Укажите путь к вашему файлу Excel
    file_path = filedialog.askopenfilename()
    # Открываем файл Excel
    workbook = load_workbook(file_path)
    # Получаем активный лист
    sheet = workbook.active
    # Создание нового файла Excel
    wb = Workbook()
    # Активация активного листа
    ws = wb.active
    # Запись заголовка
    ws.append(['ФИО', 'Дата'])
    # Устанавливаем шрифт для текста в указанных ячейках выравнивает их по центру
    cells_to_format_font = ['A1', 'B1']
    for cell in cells_to_format_font:
        ws[cell].font = Font(size=20, bold=True)
        ws[cell].alignment = Alignment(horizontal='center', vertical='center')
    # изменяем ширину колонки
    cells_to_format_size = ['A', 'B']
    for cell in cells_to_format_size:
        ws.column_dimensions[cell].width = 30
        ws.column_dimensions[cell].font = Font(size=14)

    list_data = {}

    # Проходимся по каждой строке и выводим значения ячеек в список
    for row in sheet.iter_rows(values_only=True):
        if row[0] in surname_list:
            i = 0
            list_data[row[0]] = []
            for data in row[1:]:
                i += 1
                if data is not None:
                    list_data[row[0]].append(str(i))

    # Переносит список в ексель
    for surname, data_list in list_data.items():
        data_str = [', '.join(data_list)]
        row_data = [surname] + data_str
        ws.append(row_data)

    # Сохранение файла
    file_name = '106.xlsx'
    wb.save(file_name)


surname_list = []

win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title("Парсер по 106-ой")
icon = tk.PhotoImage(file='cleaning_icon.png')
win.iconphoto(False, icon)
win.config(bg='#8FBC8F')
win.resizable(False, False)

label = tk.Label(text="Создание списка по 106-й",
                 bg='#8FBC8F',
                 font=('Arial', 20, 'italic', 'bold'),
                 )

btn1 = tk.Button(win, text='Выберете Фамилии',
                 command=open_file_surnames,
                 )

btn2 = tk.Button(win, text='Генерация',
                 command=generation_file_list,
                 )

label.pack()
btn1.pack()
btn2.pack()
print()

win.mainloop()
