from number_systems import convert_base


def pow(n, p):
    tmp = 1
    for i in range(p):
        tmp *= n
    return tmp


check = 1
while True:
    a = pow(4, 2015) + pow(2, check) - pow(2, 2015) + 15
    _sum = 0
    for i in convert_base(a, 10, 2):
        if i == '1':
            _sum += 1
    if _sum == 500:
        break
    check += 1
print(check)
