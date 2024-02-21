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


# Общие сноски:
# Разобраться с тем что при вводе отрицательного числа ни чего не выходит

def menu():
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
    decoration_2('')
    decoration_2("Выберете пункт меню:")
    decoration_2("  1)Начать игру")
    decoration_2("  2)Таблица рекордов")
    decoration_2("  3)Помощь", )
    decoration_2("  4)Выход")
    decoration('', '-')
    number = fool_protect_menu(input("Выберете номер в меню: "))  # Первая проверка числа, первое входное значение
    if number == 1:
        menu_level()
    elif number == 2:
        pass
    elif number == 3:
        print(Help)
        time.sleep(1)
        menu()
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
    number = fool_protect_menu(input("Выберете номер в меню: "))  # Последующие проверки введенного числа в цикле
    if number == 1:
        easy = 31
        new_game(easy)
    elif number == 2:
        normal = 51
        new_game(normal)
    elif number == 3:
        hard = 100
        new_game(hard)
    elif number == 4:
        menu(game_num)


def new_game(lvl, new_game_num=1):
    again_game = True
    random_num = int(randint(1, lvl))
    attempt = 0
    while again_game:
        decoration(f"Игра №{new_game_num}", '-')
        print("TEST", random_num)
        attempt += 1
        again_game, random_num, attempt, new_game_num = check_answer(random_num, is_valid(lvl, attempt), attempt, lvl,
                                                                     new_game_num)


def check_answer(random_num, answer_number, attempt, lvl, new_game_num):
    """
    Сверка ответа с введенным числом.
    :return:
    """
    if answer_number < random_num:
        print("Ваше число меньше загаданного\n")
        return True, random_num, attempt, new_game_num
    elif answer_number > random_num:
        print("Ваше число больше загаданного\n")
        return True, random_num, attempt, new_game_num
    else:
        print(f"Вы угадали за {attempt} попыток, поздравляем!\n")
        decoration('', '-')
        choice = input("Вы хотите продолжить игру?\n 1)Да\n 2)Нет\n")
        if choice == "1":
            new_game_num += 1
            return True, int(randint(1, lvl)), 0, new_game_num
        elif choice == "2":
            return False, None, None, None
        else:
            print("Неверный ввод.\nПожалуйста, введите 1 для продолжения или 2 для выхода.\n")
            return check_answer(random_num, answer_number,
                                attempt, lvl, new_game_num)  # Рекурсивный вызов функции для обработки неверного ввода


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


def is_valid(lvl, attempt):
    """
    Проверяет введенное значение на валидность.
    :return:
    """
    while True:
        answer = input(f"Попытка №{attempt}\nВведите число:\n")
        decoration('Результат', '-')
        print()
        try:
            if int(answer) and int(answer) in range(1, lvl):
                break
            else:
                print(f"Введите число от {0} до {lvl - 1}")
        except ValueError:  # ValueError Указывает на явную ошибку ввода текста
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
    menu()
