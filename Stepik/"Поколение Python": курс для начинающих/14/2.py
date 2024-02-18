# https://stepik.org/lesson/334152/step/5?unit=317561
def get_shipping_cost(quantity):
    """
    Считает по цене 1000 рублей за первый товар и
    120 рублей за каждый последующий товар.
    :return:
    """
    return print(1000 + (quantity - 1) * 120)

get_shipping_cost(int(input()))