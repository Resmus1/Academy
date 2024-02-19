# https://stepik.org/lesson/349845/step/1?unit=333700
import time

Help = """
Это игра, в которой требуется угадать число,
загаданное компьютером в диапазоне чисел от 1 до 100. После ввода числа
даётся информация, больше или меньше введенное число, чем загаданное,
и так до тех пор, пока число не будет угадано. По завершению
игра показывает среднее арифметическое число попыток для диапазона.'
"""  # Переписать правила игры!!!!


def menu(game_num):
    """
    Меню для взаимодействия с пользователем.
    1. Начать игру
    2. Таблица счета за все игры
    3. Помощь
    4. Выход из игры

    :return:
    """
    decoration('Меню', '-')
    decoration("Добро пожаловать в Игру", ' ')
    decoration(f"Игра №{game_num}", ' ')
    decoration_2("Выберете пункт меню:")
    decoration_2("  1)Начать игру")
    decoration_2("  2)Таблица рекордов")
    decoration_2("  3)Помощь", )
    decoration_2("  4)Выход")
    decoration('', '-')
    number = fool_protect_menu(input("Выберете номер в меню: "))
    if number == 1:
        menu_level(game_num)
    elif number == 2:
        pass
    elif number == 3:
        print(Help)
        time.sleep(1)
        menu(game_num)
    elif number == 4:
        print("Спасибо за игру!")
        time.sleep(1)
        exit()


def menu_level(game_num):
    """
    Меню выбора сложности:
    1)Легкая: до 30
    2)Средняя: до 50
    3)Тяжелая: до 100
    :return:
    """
    decoration('Меню', '-')
    decoration_2("Выберете сложность игры:")
    decoration_2("  1)Легкая: до 30")
    decoration_2("  2)Средняя: до 50")
    decoration_2("  3)Тяжелая: до 100")
    decoration_2("  4)Назад в меню")
    decoration('', '-')
    number = fool_protect_menu(input("Выберете номер в меню: "))
    if number == 1:
        pass
    elif number == 2:
        pass
    elif number == 3:
        pass
    elif number == 4:
        menu(game_num)


def fool_protect_menu(number):
    """
    Является ли значение числом из меню.
    :return:
    """
    flag = True
    while flag:
        try:
            if int(number) and int(number) in range(1, 5):
                flag = False
            elif int(number) < 0 or int(number) > 4:
                print("Введен не верный номер, введите номер из меню")
                number = input("Выберете номер в меню: ")
        except:
            if number.isalpha():
                print("Введены буквы, введите номер из меню")
                number = input("Выберете номер в меню: ")
            else:
                print("Введены непонятные символа, введите номер из меню")
                number = input("Выберете номер в меню: ")
    return int(number)


def decoration(word, symbol):
    """
    Полосочка для декорации в меню.
    Указывается параметр, который будет по центру линий.
    :return:
    """
    print('-', end='')
    line = int((36 - len(word)) / 2)
    [print(symbol, end='') for _ in range(line)]
    print(word, end='')
    if len(word) % 2 != 0:
        line += 1
    [print(symbol, end='') for _ in range(line)]
    print('-', end='')
    print()


def decoration_2(word):
    """
    Выравнивает текст в меню по левому краю и создает общую рамку.
    :return:
    """
    print('-', end='')
    print(' ', word, end='')
    print(' ' * (33 - len(word)), '-')


def score():
    """
    Считает очки, создает таблицу лидеров.
    :return:
    """
    pass


def is_valid():
    """
    Проверяет введенное значение на валидность.
    Требования: Число от 1-1000 в зависимости от сложности
    :return:
    """
    pass


def game():
    pass


game_number = 0  # Счетчик количество игр

menu(game_number)
