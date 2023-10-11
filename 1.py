# Задание 1
# 1
x = int(input('Введите число от 1 до 9:\n'))
# 2
if 1 <= x <= 3:
    s = input("Введите строку:\n")
    n = int(input("Введите число повторов:\n"))
    for _ in range(n):
        print(s)
# 3
elif 4 <= x <= 6:
    m = int(input("Введите степень, в которую возвести число\n"))
    print(pow(x, m))
# 4
elif 7 <= x <= 9:
    for _ in range(10):
        x += 1
    print(x)
else:
    print('Ошибка ввода')
