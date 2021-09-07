from number_systems import convert_base


def pow(n, p):
    tmp = 1
    for i in range(p):
        tmp *= n
    return tmp


res = 0
a = format(pow(7, 103) + 6 * pow(7, 104) - 3 * pow(7, 57) + 98, '.0f')
print('Результат в 10 СС:', a)
a = convert_base(a, 10, 7)
print('Результат в 7 СС:', a)
for i in a:
    res += int(i)
print('Сумма цифр числа:', res)
