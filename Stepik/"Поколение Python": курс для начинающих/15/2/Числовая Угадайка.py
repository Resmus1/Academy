# https://stepik.org/lesson/349845/step/1?unit=333700
import time
from random import randint

Help = """
Это игра, в которой требуется угадать число,
Здесь есть выбор сложности каждая сложность дает разное количество очков
После ввода числа даётся информация, больше или меньше введенное число, чем загаданное,
и так до тех пор, пока число не будет угадано или попытки не закончатся.
"""

player_score = {}


def menu():
    """
    Меню для взаимодействия с пользователем.
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
    number = fool_protect_menu(input("Выберете номер в меню: "))
    if number == 1:
        name_player = input("Введите свое имя: ")
        if name_player in player_score:
            menu_level(name_player)
        else:
            player_score[name_player] = 0
            menu_level(name_player)
    elif number == 2:
        decoration('Рекорды', '-')
        sorted_player_score = sorted(player_score.items(),
                                     key=lambda x: x[1], reverse=True)
        for index, (name, score) in enumerate(sorted_player_score):
            print(f"{index + 1}. {name} = {score} очков.")
        print()
    elif number == 3:
        print(Help)
        menu()
    elif number == 4:
        print("Спасибо за игру!")
        time.sleep(1)
        exit()


def menu_level(name_player):
    """
    Меню выбора сложности
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
        easy = 30
        score = new_game(easy)
        player_score[name_player] += score
        print(f"Ваши очки за эту игру: {score}")
    elif number == 2:
        normal = 50
        score = new_game(normal)
        player_score[name_player] += score * 2
        print(f"Ваши очки за эту игру: {score * 2}")
    elif number == 3:
        hard = 100
        score = new_game(hard)
        player_score[name_player] += score * 3
        print(f"Ваши очки за эту игру: {score * 3}")
    elif number == 4:
        menu()


def new_game(lvl, new_game_num=1):
    """
    Новая Игра.
    """
    again_game = True
    random_num = int(randint(1, lvl))
    attempt = 0
    while again_game:
        decoration(f"Игра №{new_game_num}", '-')
        print("TEST", random_num)
        attempt += 1
        again_game, random_num, attempt, new_game_num = check_answer(
            random_num, is_valid(lvl, attempt), attempt, lvl, new_game_num)
    return new_game_num


def check_answer(random_num, answer_number, attempt, lvl, new_game_num):
    """
    Сверка ответа с введенным числом.
    """
    if attempt >= 7:
        decoration("Вы проиграли!", '-')
        decoration(f"Вы сыграли {new_game_num} игр", '-')
        print()
        return False, None, None, new_game_num - 1
    elif answer_number < random_num:
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
            return False, None, None, new_game_num
        else:
            print("Неверный ввод.\nПожалуйста, введите 1 "
                  "для продолжения или 2 для выхода.\n")
            return check_answer(random_num, answer_number,
                                attempt, lvl, new_game_num)


def fool_protect_menu(number):
    """
    Является ли значение числом из меню.
    """
    work = True
    while work:
        try:
            if int(number) and int(number) in range(1, 5):
                work = False
            elif int(number) < 0 or int(number) > 4:
                print("Введен не верный номер")
                number = input("Выберете номер в меню: ")
        except ValueError:
            if number.isalpha():
                print("Введены буквы")
                number = input("Выберете номер в меню: ")
            else:
                print("Введены непонятные символа")
                number = input("Выберете номер в меню: ")
    return int(number)


def is_valid(lvl, attempt):
    """
    Проверяет введенное значение на валидность.
    """
    while True:
        answer = input(f"Осталось {8 - attempt} попыток.\nВведите число:\n")
        decoration('Результат', '-')
        print()
        try:
            if int(answer) and int(answer) in range(1, lvl):
                break
            else:
                print(f"Введите число от {1} до {lvl - 1}")
        except ValueError:
            if answer.isalpha():
                print("Введены буквы")
            else:
                print("Введены непонятные символа")
    return int(answer)


def decoration(word, symbol):
    """
    Полосочка для декорации в меню.
    Указывается параметр, который будет по центру линий.
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
    """
    print('-', end='')
    print(' ', word, end='')
    print(' ' * (33 - len(word)), '-')


while True:
    menu()
