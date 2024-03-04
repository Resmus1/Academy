import random

Help = "Игра в висельника"

words = ['ABCDABCD']


def enter():
    """
    Обработка ввода проверка на то что введена одна буква
    """
    while True:
        char = input("\nВведите одну букву:\n=>").strip().upper()
        if char.isalpha() and len(char) == 1:
            return char


def game(word, letter):
    """
    Проверка правильности введенного значения
    """
    global tries
    global count_right
    found = hidden_word.count(letter) > 0
    if found:
        for i_letter in word:
            if i_letter == letter:
                count_right += 1
                i = word.index(i_letter)
                word[i], answer[i] = answer[i], word[i]
    else:
        tries -= 1
    return display_hangman()


def end_game():
    global tries
    if tries == 0:
        print("Вы проиграли!")
        exit()
    elif count_right == len(hidden_word):
        print("Вы выиграли, Поздравляем!")
        exit()


def display_hangman():
    global tries
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',

        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',

        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',

        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',

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


tries = 6
count_right = 0
hidden_word = list(random.choice(words))
answer = ['_' for _ in range(len(hidden_word))]

while True:
    print(f"{game(hidden_word, enter())}\n{' '.join(answer)}\n")
    end_game()
