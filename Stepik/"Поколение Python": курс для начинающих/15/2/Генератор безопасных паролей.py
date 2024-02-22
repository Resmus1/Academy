# https://stepik.org/lesson/349848/step/1?unit=333703
import random

data_password = {
    'digits': '0123456789',
    'lowercase_letters': 'abcdefghijklmnopqrstuvwxyz',
    'uppercase_letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'symbol': '!#$%&*+-=?@^_',
    'symbol_remove': 'il1Lo0O'
}


def check_input(text, valid_inputs):
    user_input = input(text).lower()
    while user_input not in valid_inputs:
        print(f"Введите одно из следующих: {', '.join(valid_inputs)}")
        user_input = input(text).lower()
    return user_input


def check_num(text, max_length):
    while True:
        try:
            num = int(input(text))
            if num < max_length:
                return num
            print(f"Максимальное значение должно быть {max_length}\n")
        except ValueError:
            print('Введите цифры!')


def generate_password(count, length, enable_num, enable_up, enable_low, enable_symbol, disable_similar_symbol):
    password = ''
    password += data_password['digits'] if enable_num == 'yes' else ''
    password += data_password['uppercase_letters'] if enable_up == 'yes' else ''
    password += data_password['lowercase_letters'] if enable_low == 'yes' else ''
    password += data_password['symbol'] if enable_symbol == 'yes' else ''
    if disable_similar_symbol == 'yes':
        for symbol in data_password['symbol_remove']:
            password = password.replace(symbol, '')
    for _ in range(count):
        print(''.join(random.choices(password, k=length)))


generate_password(check_num("Количество паролей для генерации\n", 100),
                  check_num("Длина одного пароля\n", 36), check_input("Включать ли цифры? (yes/no)\n", ['yes', 'no']),
                  check_input("Включать ли прописные буквы? (yes/no)\n", ['yes', 'no']),
                  check_input("Включать ли строчные буквы? (yes/no)\n", ['yes', 'no']),
                  check_input("Включать ли символы? (yes/no)\n", ['yes', 'no']),
                  check_input("Исключать ли неоднозначные символы? (yes/no)\n", ['yes', 'no']))
