from number_systems import convert_base


def pow(n, p):
    tmp = 1
    for i in range(p):
        tmp *= n
    return tmp


check = 1
while True:
    a = pow(36, 17) - pow(6, check) + 71
    _sum = 0
    for i in convert_base(a, 10, 6):
        _sum += int(i)
    if _sum == 61:
        break
    check += 1
print(check)
