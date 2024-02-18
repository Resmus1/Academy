# https://stepik.org/lesson/334150/step/5?unit=317559
def is_password_good(password):
    """
    Проверяет пароль на следующие правила:
    1. его длина не менее 8 символов;
    2. он содержит как минимум одну заглавную букву (верхний регистр);
    3. он содержит как минимум одну строчную букву (нижний регистр);
    4. он содержит хотя бы одну цифру.
    :return:
    """
    upper = False
    lower = False
    num = False
    if len(password) < 8:
        return False
    for i in password:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
        if i.isdigit():
            num = True
    return upper and lower and num


print(is_password_good(input()))
