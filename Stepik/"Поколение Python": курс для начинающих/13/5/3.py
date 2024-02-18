# https://stepik.org/lesson/334150/step/4?unit=317559
def get_next_prime(n):
    """
    Выдает последующее простое число.
    Подается число и проверяется от 2 до n-1 и
    не является ли оно уже простым
    :return:
    """
    first_n = n
    while True:
        if n == 1:
            n += 1
        for i in range(2, n):
            if n % i == 0:
                n += 1
                continue
        if n == first_n:
            n += 1
            continue
        if n % 1 == 0 and n % n == 0:
            return print(n)


get_next_prime(int(input()))
