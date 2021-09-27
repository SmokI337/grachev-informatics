def exponent(n):
    if not 'e' in str(n):
        return n
    num = str(n)
    check = int(num[num.index('e') + 2: len(num)])
    num = num[0: num.index('e')]
    if '.' in num:
        a, b = num.split('.')
        check += len(b)
    return '{:0.{check}f}'.format(n, check=check)


def convert_base(num, from_base=10, to_base=10, again=False):
    try:
        from_base = int(from_base)
    except:
        return 'Ошибка: введите корректное значение системы'

    try:
        to_base = int(to_base)
    except:
        return 'Ошибка: введите корректное значение системы'

    num = str(exponent(num))

    for i in num:
        if i.islower():
            num = num.replace(i, i.upper())

    isNegative = False
    if num.count('-') > 1:
        return 'Ошибка: число содержит недопустимые для системы счисления символы'
    elif '-' in num:
        num = num.replace('-', '')
        isNegative = True

    if num.count('.') > 1 or num.count(',') > 1:
        return 'Ошибка: введите корректную дробь'

    if ',' in num:
        num = num.replace(',', '.')

    frac = ''
    if '.' in num:
        num, frac = num.split('.')

    if frac.count('(') == 1 and frac.count(')') == 1:
        copy = frac[frac.find('(') + 1: frac.find(')')]
        frac = frac.replace('(', '').replace(')', '').replace(copy, '')
        while len(frac) < 60:
            frac += copy
    elif frac.count('(') > 1 or frac.count(')') > 1:
        return 'Ошибка: введите корректную дробь'

    if frac == '0':
        frac = ''

    if num == '0' and frac == '':
        return '0'

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
        if isNegative:
            return '-' + num + '.' + frac
        else:
            return num + '.' + frac
    elif from_base == to_base and frac == '':
        if isNegative:
            return '-' + num
        else:
            return num

    if from_base == 10 and to_base != 10:
        res, num = '', int(num)
        while num > 0:
            plus = chr(55 + num % to_base) if num % to_base > 9 else num % to_base
            res = str(plus) + res
            num //= to_base
        if frac != '':
            if res == '':
                res += '0.'
            else:
                res += '.'
            frac = float('0.' + frac)
            n = 0
            while True:
                frac *= to_base
                tmp, frac_tmp = str(exponent(frac)).split('.')
                frac = float('0.' + frac_tmp)
                tmp = int(tmp)
                res += chr(55 + tmp) if tmp % to_base > 9 else str(tmp)
                if frac_tmp == '0':
                    res = str(res).strip('0')
                    if isNegative:
                        return '-' + res
                    else:
                        return res
                if n > 10 and res.split('.')[1] != '0':
                    break
                n += 1
            res = str(res).strip('0')
            if not again:
                res, s = res.split('.')
                i = (s + s).find(s, 1, -1)
                if i != -1:
                    res += '.(' + s[:i] + ')'
                else:
                    res += '.' + s + ' (округлено)'
        if isNegative:
            return '-' + res
        else:
            return res

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
            res = str(res).strip('0')
            if not again:
                res, s = res.split('.')
                i = (s + s).find(s, 1, -1)
                if i != -1:
                    res += '.(' + s[:i] + ')'
                else:
                    res += '.' + s
        if isNegative:
            return '-' + res
        else:
            return res

    elif from_base != 10 and to_base != 10:
        if isNegative:
            return '-' + convert_base(convert_base(num + '.' + frac, from_base, 10, True), 10, to_base)
        else:
            return convert_base(convert_base(num + '.' + frac, from_base, 10, True), 10, to_base)

# from_base, to_base, num = input().split()
# print(convert_base(num, from_base, to_base))
