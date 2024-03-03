import random

Help = "Игра в висельника"

words = ['ABCDABCD']


def enter():
    """
    Обработка ввода проверка на то что введена одна буква
    """
    while True:
        char = input("Введите одну букву:\n").upper()
        if char.isalpha() and len(char) == 1:
            return char


def right(word, letter):
    """
    Проверка правильности введенного значения
    """
    global tries
    found = True if letter in word else False
    if found:
        for i_letter in word:
            if i_letter == letter:
                i = word.index(i_letter)
                word[i], answer[i] = answer[i], word[i]
    else:
        tries -= 1
    return display_hangman()


def end_game():
    global tries
    if tries == 0:
        print("Вы проиграли")
        exit()


# функция получения текущего состояния
def display_hangman():
    global tries
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def game(word):
    """
    Игра
    """
    pass


hidden_word = list(random.choice(words))
answer = ['_' for i in range(7)]
tries = 6


while True:
    enter_letter = enter()
    print(right(hidden_word, enter_letter))
    print(answer)
    end_game()
