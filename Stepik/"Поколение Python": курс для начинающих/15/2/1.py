# https://stepik.org/lesson/349845/step/1?unit=333700
from math import log2, ceil
from random import randint
import time


# Доработать меню
# Поставить проверку дурака на yes no

def menu(g_cnt):
    '''
    Меню для взаимодействия с пользователем
    :return:
    '''
    print(f"----------------Меню----------------\nДобро пожаловать в числовую угадайку\n"
          f"               Игра №{g_cnt}\nВыберете пункт меню:\n  1)Начать игру\n  2)Помощь\n"
          f"  3)Выход\n------------------------------------")
    temp_key = is_valid()
    if temp_key:
        while True:
            temp_key = int(temp_key)
            if temp_key == 1:
                break
            elif temp_key == 2:
                print(f"{HELP}\nПродолжить YES/NO?")
                yes_no = is_valid_yes_no()
                if yes_no:
                    break
                elif not yes_no:
                    exit()
            elif temp_key == 3:
                exit()


            else:
                print("Введите № пункта в меню.")
    else:
        print('NOOOOO')


def is_valid_yes_no():
    """
    Проверяет Да или Нет на валидность
    :return:
    """
    while True:
        yes_no = input().upper()
        if yes_no == 'YES' or yes_no == 'Y':
            return True
        elif yes_no == 'NO' or yes_no == 'N':
            return False
        else:
            print("Продолжить YES/NO?")


def is_valid():
    """
    Проверяет введенное значение,
    является ли значение целым числом и от 1 до 100
    :return:
    """
    while True:
        number = input("Введите число:\n")
        try:
            if int(number) and int(number) in range(1, 101):
                break
            elif int(number) > 0 or int(number) > 100:
                print("Введено значение больше или меньше 100")
        except:
            if number.isalpha():
                print("Введены буквы")
            else:
                print("Введены непонятные символа")
    return number


def check_answer(answer_number):
    """
    Сверка ответа с введенным числом.
    :return:
    """
    answer_number = int(answer_number)
    if answer_number < random_num:
        print("Ваше число меньше загаданного, попробуйте еще разок")
    elif answer_number > random_num:
        print("Ваше число больше загаданного, попробуйте еще разок")
    else:
        print("Вы угадали, поздравляем!\nПродолжить игру?")
        next = is_valid_yes_no()
        if next:
            return True
        elif not next:
            menu(game_count)


HELP = """
Это игра, в которой требуется угадать число,
загаданное компьютером в диапазоне чисел от 1 до 100. После ввода числа
даётся информация, больше или меньше введенное число, чем загаданное,
и так до тех пор, пока число не будет угадано. По завершению
игра показывает среднее арифметическое число попыток для диапазона.'
"""

# time.sleep(0.5)
game_count = 0  # Счетчик количества игр
attempt = 0  # Счётчик количества попыток
menu(game_count)
print(f"Добро пожаловать в числовую угадайку.\nИгра №{game_count}\n--------------------------")
random_num = int(randint(1, 100))
while True:
    print(f"Это число!, {random_num}\nПопытка №{attempt}")
    answer = is_valid()
    attempt += 1
    if answer:
        if check_answer(answer):
            game_count += 1
            attempt = 0
        else:
            game_count = 0 # Доработать не хочет считать нормально!
#
# # print(ceil(log2(randint(1, 101))))
