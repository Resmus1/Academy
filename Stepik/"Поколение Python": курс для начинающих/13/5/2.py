# https://stepik.org/lesson/334150/step/3?unit=317559
def is_prime(n):
    """
    Проверка на то простое ли число
    1. Равно ли число единице.
    2. Простое ли оно
    :return:
    """
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False


n = int(input())

print(is_prime(n))
