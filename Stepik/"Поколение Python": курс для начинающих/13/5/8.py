# https://stepik.org/lesson/334150/step/9?unit=317559
def is_correct_bracket(text):
    """
    Принимает в качестве аргумента непустую строку text, состоящую из символов '(' и ')'
    и возвращает значение True, если поступившая на вход строка
    является правильной скобочной последовательностью и False в противном случае.
    :return:
    """
    cnt = 0
    for i in text:
        if i == ')':
            cnt -= 1
        elif cnt < 0:
            return print(False)
        elif i == '(':
            cnt += 1
    if cnt != 0:
        return print(False)
    return print(True)


is_correct_bracket(input())