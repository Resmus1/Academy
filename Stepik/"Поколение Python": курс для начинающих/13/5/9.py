# https://stepik.org/lesson/334150/step/10?unit=317559
def convert_to_python_case(text):
    """
    Принимает в качестве аргумента строку в «верблюжьем регистре»
    и преобразует его в «змеиный регистр».
    :return:
    """
    new_text = ''
    for i in text:
        if i.isupper():
            new_text += '_' + i.lower()
            continue
        new_text += i

    return print(new_text[1:])


convert_to_python_case(input())
