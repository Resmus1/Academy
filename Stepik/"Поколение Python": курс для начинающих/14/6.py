# https://stepik.org/lesson/334152/step/9?unit=317561
def is_magic(date):
    '''
    Принимает в качестве аргумента строковое представление
    корректной даты и возвращает значение True,
    если дата является магической и False - в противном случае.
    :return:
    '''

    if date[0] * date[1] == date[2] % 100:
        return print(True)
    return print(False)


is_magic(list(map(int, input().split('.'))))
