# https://stepik.org/lesson/349846/step/1?unit=333701
import random


answers = ("Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно")


def hello():
    """
    Приветствует и запрашивает имя
    """
    return input("Привет, я магический шар,и я знаю ответ на любой твой вопрос.\nКак Вас зовут?\n")


def next_question():
    while True:
        question = input("У вас остались еще вопросы? (Yes / No)\n").lower()
        if question in ('yes', 'y'):
            return True
        elif question in ('no', 'n'):
            print("Возвращайся если возникнут вопросы!")
            return False
        else:
            print("Вы ввели неверный ответ.")


name = hello()
input(f"Привет, {name}! Задавай свой вопрос.\n")
print(random.choice(answers))
while next_question():
    print(random.choice(answers))