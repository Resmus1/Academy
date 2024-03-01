def num_to_sign(num):
    base_more_10 = ['A', 'B', 'C', 'D', 'E', 'F']
    if num < 10:
        return str(num)
    else:
        return base_more_10[num - 10]


def calculator_from_10(n, base):
    """
    Перевод чисел из десятичной системы счисления в любую другую
    """
    result_reversed = []
    while n // (base - 1) > 0:
        result_reversed.append(num_to_sign(n % base))
        n = n // base
    if num_to_sign(n) == "0":
        result = "".join(result_reversed[::-1])
    else:
        result = num_to_sign(n) + "".join(result_reversed[::-1])
    return result


num = int(input("Введите число:\n"))
numer = int(input("Введите систему в которую нужно перевести:\n"))
print(calculator_from_10(num, numer))
