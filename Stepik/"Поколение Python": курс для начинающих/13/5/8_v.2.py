# https://stepik.org/lesson/334150/step/9?unit=317559
def is_correct_bracket(text):
    """
    Принимает в качестве аргумента непустую строку text, состоящую из символов '(' и ')'
    и возвращает значение True, если поступившая на вход строка
    является правильной скобочной последовательностью и False в противном случае.
    :return:
    """
    while "()" in text:
        text = text.replace("()", "")
    return print(text == "")


is_correct_bracket(input())