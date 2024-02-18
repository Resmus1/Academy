# https://stepik.org/lesson/349845/step/1?unit=333700

import time


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
    number = fool_protect_menu()
    if number == 1:
        print(1)
    elif number == 2:
        print(2)
    elif number == 3:
        print(3)
    elif number == 4:
        print("Спасибо за игру!")
        time.sleep(1)
        exit()


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


def fool_protect_menu():
    """
    Является ли значение числом из меню.
    :return:
    """
    flag = True
    while flag:
        number = input("Выберете номер в меню: ")
        try:
            if int(number) and int(number) in range(1, 5):
                flag = False
            elif int(number) < 0 or int(number) > 4:
                print("Введен не верный номер, введите номер из меню")
        except:
            if number.isalpha():
                print("Введены буквы, введите номер из меню")
            else:
                print("Введены непонятные символа, введите номер из меню")
    return int(number)



def game():
    pass


def level():
    pass


game_number = 0  # Счетчик количество игр

menu(game_number)
