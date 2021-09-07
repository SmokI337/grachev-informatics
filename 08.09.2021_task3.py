from number_systems import convert_base


def pow(n, p):
    tmp = 1
    for i in range(p):
        tmp *= n
    return tmp


res = 0
a = format(pow(81, 18) - (pow(81, 8) - 1) * (pow(9, 8) + 1) / 8 - 8, '.0f')
print('Результат в 10 СС:', a)
a = convert_base(a, 10, 3)
print('Результат в 3 СС:', a)
for i in a:
    if i == '1':
        res += 1
print('Количество единиц в записи:', res)
