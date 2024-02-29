# https://stepik.org/lesson/415553/step/7?unit=405082

num = input()

if len(num) == 6:
    print(int(num[0] + num[:0:-1]))
else:
    print(int(num[:-5]))
