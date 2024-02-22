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
    while True:
        user_input = input(text).lower()
        if user_input in valid_inputs:
            return user_input
        print(f"Введите одно из следующих: {', '.join(valid_inputs)}")


def check_num(text, max_length):
    while True:
        try:
            num = int(input(text))
            if num < max_length:
                return num
            else:
                print(f"Максимальное значение должно быть {max_length}")
        except ValueError:
            print('Введите цифры!')


def generate_password(length, enable_num, enable_up, enable_low, enable_symbol, disable_similar_symbol):
    password = ''
    if enable_num == 'yes':
        password += data_password['digits']
    if enable_up == 'yes':
        password += data_password['uppercase_letters']
    if enable_low == 'yes':
        password += data_password['lowercase_letters']
    if enable_symbol == 'yes':
        password += data_password['symbol']
    if disable_similar_symbol == 'yes':
        for symbol in data_password['symbol_remove']:
            password = password.replace(symbol, '')
    return ''.join(random.choices(password, k=length))


question_password = {
    'passwords': check_num("Количество паролей для генерации\n", 100),
    'length': check_num("Длина одного пароля\n", 36),
    'enable_num': check_input("Включать ли цифры? (yes/no)\n", ['yes', 'no']),
    'enable_up': check_input("Включать ли прописные буквы? (yes/no)\n", ['yes', 'no']),
    'enable_low': check_input("Включать ли строчные буквы? (yes/no)\n", ['yes', 'no']),
    'enable_symbol': check_input("Включать ли символы? (yes/no)\n", ['yes', 'no']),
    'disable_similar_symbol': check_input("Исключать ли неоднозначные символы? (yes/no)\n", ['yes', 'no'])
}
# question_password = {'passwords': 3, 'length': 8, 'enable_num': 'no', 'enable_up': 'yes', 'enable_low': 'yes', 'enable_symbol': 'yes', 'disable_similar_symbol': 'yes'}


for _ in range(question_password['passwords']):
    print(generate_password(question_password['length'],
                             question_password['enable_num'],
                             question_password['enable_up'],
                             question_password['enable_low'],
                             question_password['enable_symbol'],
                             question_password['disable_similar_symbol']))
