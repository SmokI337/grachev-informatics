def convert_base(num, from_base=10, to_base=10):
    for i in num:
        if i.islower():
            num = num.replace(i, i.upper())

    if num == '0':
        return '0'

    if from_base == to_base:
        return num

    if from_base == 10 and to_base != 10:
        res, num = '', int(num)
        while num > 0:
            plus = chr(55 + num % to_base) if num % to_base > 9 else num % to_base
            res = str(plus) + res
            num //= to_base
        return res

    elif from_base != 10 and to_base == 10:
        res, num = 0, str(num)
        for i in range(len(num)):
            if num[len(num) - 1 - i].isalpha():
                res += (ord(num[len(num) - 1 - i]) - 55) * (from_base ** i)
            else:
                res += int(num[len(num) - 1 - i]) * (from_base ** i)
        return res

    elif from_base != 10 and to_base != 10:
        return convert_base(convert_base(num, from_base, 10), 10, to_base)


num, from_base, to_base = input().split()
print(convert_base(num, int(from_base), int(to_base)))