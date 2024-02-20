# https://stepik.org/lesson/349845/step/1?unit=333700
import time
from random import randint

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
        menu_level()
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


def menu_level():
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
        # Создать цикл повтора и вывести в функцию
        random_num = int(randint(1, 31))
        print(random_num)
        while check_answer(random_num, is_valid()):
            pass
            # count_game += 1  # создать счетчик не работает
        # s = input("Продолжить игру?")
        # if s == 1:
        #     check_answer(random_num, is_valid())

        # attempt = 0
        # number = input()
        # print(number)
        # while True:
        #     print(f"Это число!, {random_num}\nПопытка №{attempt}")
        #     number = is_valid()
        #     attempt += 1
        # if answer:
        #     if check_answer(answer):
        #         game_count += 1
        #         attempt = 0
        #     else:
        #         game_count = 0  # Доработать не хочет считать нормально!

    elif number == 2:
        pass
    elif number == 3:
        pass
    elif number == 4:
        menu(game_num)


def check_answer(random_num, answer_number):
    """
    Сверка ответа с введенным числом.
    :return:
    """
    if answer_number < random_num:
        print("Ваше число меньше загаданного, попробуйте еще разок")
        return True
    elif answer_number > random_num:
        print("Ваше число больше загаданного, попробуйте еще разок")
        return True
    else:
        print("Вы угадали, поздравляем!\n")
        return False
    # Разобраться с прохождением дальше по игре и количеству игр
    #     next = is_valid_yes_no()
    #     if next:
    #         return True
    #     elif not next:
    #         menu(game_count)


def fool_protect_menu(number):
    """
    Является ли значение числом из меню.
    :return:
    """
    work = True
    while work:
        try:
            if int(number) and int(number) in range(1, 5):
                work = False
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


def is_valid():
    """
    Проверяет введенное значение,
    cоответствует ли значение ответу и параметрам
    :return:
    """
    while True:
        answer = input("Введите число:\n")
        try:
            if int(answer) and int(answer) in range(1, 31):
                break
            elif int(answer) > 0 or int(answer) > 30:
                print("Введено значение больше или меньше 30")
        except:
            if answer.isalpha():
                print("Введены буквы")
            else:
                print("Введены непонятные символа")
    return int(answer)


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


def game():
    pass


game_number = 0  # Счетчик количество игр
# count_game = 0  # Считает количество игр в режиме

while True:
    menu(game_number)
