# https://stepik.org/lesson/334150/step/4?unit=317559
def is_prime(num):
    """
    Проверяет равняться ли числ единице и является ли простым.
    :return:
    """
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_next_prime(num):
    """
    Ищем следующее простое число.
    :return:
    """
    cur_num = num + 1
    while not is_prime(cur_num):
        cur_num += 1
    return cur_num


print(get_next_prime(int(input())))