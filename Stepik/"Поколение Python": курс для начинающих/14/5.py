# https://stepik.org/lesson/334152/step/8?unit=317561
def get_month(language, number):
    '''
    Принимает на вход два аргумента language – язык ru или en
    и number – номер месяца (от 1 до 12)
    и возвращает название месяца на русском или английском языке.
    :return:
    '''
    d = {'ru': {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель',
                5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
                9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь', },
         'en': {1: 'january', 2: 'february', 3: 'march', 4: 'april',
                5: 'may', 6: 'june', 7: 'july', 8: 'august',
                9: 'september', 10: 'october', 11: 'november', 12: 'december', }}
    return print(d[language][number])


get_month(input(), int(input()))
