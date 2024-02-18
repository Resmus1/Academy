def is_palindrome(text):
    """
    Принимает в качестве аргумента строку text и возвращает значение True,
    если указанный текст является палиндромом и False в противном случае.
    :return:
    """
    new_text = ''
    for i in text:
        if i.isalpha():
            new_text += i
    return new_text == new_text[::-1]


print(is_palindrome(input().lower()))
