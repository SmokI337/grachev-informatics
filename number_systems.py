def convert_base(num, from_base=10, to_base=10):
    try:
       from_base = int(from_base)
    except:
        return 'Введите корректное значение исходной системы'

    try:
       to_base = int(to_base)
    except:
        return 'Введите корректное значение получаемой системы'
    
    for i in num:
        if int(i) > from_base:
            return 'Указанное число содержит недопустимые для исходной системы счисления символы'
    
    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return 'Основание системы счисления не может быть меньше 2 или больше 36'
    
    if from_base == to_base:
        return num

    if from_base == 10 and to_base != 10:
        res, num = '', int(num)
        while num > 0:
            plus = chr(65 + num % to_base - 10) if num % to_base > 9 else num % to_base
            res = str(plus) + res
            num //= to_base
        return str(res)

    elif from_base != 10 and to_base == 10:
        res, num = 0, str(num)
        for i in range(len(num)):
            if num[len(num) - 1 - i].isalpha():
                res += (ord(num[len(num) - 1 - i]) - 55) * (from_base ** i)
            else:
                res += int(num[len(num) - 1 - i]) * (from_base ** i)
        return str(res)

    elif from_base != 10 and to_base != 10:
        return convert_base(convert_base(num, from_base, 10), 10, to_base)
        

num, from_base, to_base = input().split()
print(convert_base(num, from_base, to_base))