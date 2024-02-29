# https://stepik.org/lesson/415553/step/3?unit=405082

opti = float(input()) / float(input()) ** 2

if 18.5 <= opti <= 25:
    print('Оптимальная масса')
elif opti < 18.5:
    print('Недостаточная масса')
else:
    print('Избыточная масса')
