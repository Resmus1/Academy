# https://stepik.org/lesson/334150/step/8?unit=317559
def test_num(password):
    """
    Проверяет равно ли значение 3-м цифрам.
    Число a – должно быть палиндромом.
    Число c – должно быть четным.
    :return:
    """
    password[0] = str(password[0])
    if len(password) != 3 or password[2] % 2 != 0 or password[0] != password[0][::-1]:
        return False
    return True


def is_simple(password):
    """
    Число b – должно быть простым.
    :return:
    """
    if password[1] == 1:
        return False
    for i in range(2, int(password[1] ** 0.5) + 1):
        if password[1] % i == 0:
            return False
    return True


def is_valid_password(password):
    """
    Имеет вид a:b:c, где a, b и c – натуральные числа.
    :return:
    """
    if test_num(password) and is_simple(password):
        return print(True)
    return print(False)


is_valid_password(list(map(int, input().split(':'))))
