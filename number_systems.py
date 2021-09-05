def convert_base(num, from_base=10, to_base=10, again=False):
    try:
        from_base = int(from_base)
    except:
        return 'Ошибка: введите корректное значение системы'

    try:
        to_base = int(to_base)
    except:
        return 'Ошибка: введите корректное значение системы'

    num = str(num)

    for i in num:
        if i.islower():
            num = num.replace(i, i.upper())

    if num.count('.') > 1 or num.count(',') > 1:
        return 'Ошибка: введите корректную дробь'

    frac = ''
    if '.' in num:
        num, frac = num.split('.')
    elif ',' in num:
        num, frac = num.split(',')

    if frac == '0':
        frac = ''

    for i in num:
        if i.isalpha():
            i = ord(i) - 55
        try:
            if int(i) > from_base:
                return 'Ошибка: число содержит недопустимые для системы счисления символы'
        except:
            return 'Ошибка: число содержит недопустимые для системы счисления символы'

    for i in frac:
        if i.isalpha():
            i = ord(i) - 55
        try:
            if int(i) > from_base:
                return 'Ошибка: указанное число содержит недопустимые для системы счисления символы'
        except:
            return 'Ошибка: указанное число содержит недопустимые для системы счисления символы'

    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return 'Ошибка: основание системы счисления не может быть меньше 2 или больше 36'

    if from_base == to_base and frac != '':
        return num + '.' + frac
    elif from_base == to_base and frac == '':
        return num

    if from_base == 10 and to_base != 10:
        res, num = '', int(num)
        while num > 0:
            plus = chr(55 + num % to_base) if num % to_base > 9 else num % to_base
            res = str(plus) + res
            num //= to_base
        if frac != '':
            res += '.'
            frac = float('0.' + frac)
            n = 0
            while n < 10:
                frac *= to_base
                tmp, frac_tmp = str(frac).split('.')
                frac = float('0.' + frac_tmp)
                tmp = int(tmp)
                res += chr(55 + tmp) if tmp % to_base > 9 else str(tmp)
                n += 1
                if frac_tmp == '0':
                    return str(res)
            if not again:
                res, s = res.split('.')
                i = (s + s).find(s, 1, -1)
                if i != -1:
                    res += '.(' + s[:i] + ')'
                else:
                    res += '.' + s + ' (округлено до 10 символов)'
        return str(res)

    elif from_base != 10 and to_base == 10:
        res, num = 0, str(num)
        for i in range(len(num)):
            if num[len(num) - 1 - i].isalpha():
                res += (ord(num[len(num) - 1 - i]) - 55) * (from_base ** i)
            else:
                res += int(num[len(num) - 1 - i]) * (from_base ** i)

        if frac != '':
            for i in range(0, len(frac)):
                if frac[i].isalpha():
                    res += (ord(frac[i]) - 55) * (from_base ** -(i + 1))
                else:
                    res += int(frac[i]) * (from_base ** -(i + 1))
            if not again:
                res, s = str(res).split('.')
                i = (s + s).find(s, 1, -1)
                if i != -1:
                    res += '.(' + s[:i] + ')'
                else:
                    res += '.' + s
        return str(res)

    elif from_base != 10 and to_base != 10:
        return convert_base(convert_base(num + '.' + frac, from_base, 10, True), 10, to_base)

# num, from_base, to_base = input().split()
# print(convert_base(num, from_base, to_base))
