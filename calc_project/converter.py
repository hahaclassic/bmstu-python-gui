def decimal_to_six(num):
    if num[0] == '-':
        check = True
        num = num[1:]
    else:
        check = False

    num = float(num)
    int_part = int(num//1)
    fract_part = float(num)%1
    
    # Convertation int part
    converted_num = ''
    while int_part != 0:
        converted_num += str(int_part%6)
        int_part //= 6
    if converted_num == '':
        converted_num = '0'
    converted_num = converted_num[::-1]

    # Convertation fractional part
    if fract_part != 0:
        converted_fract = ''
        k = 0
        while fract_part%1 != 0 and k < 7:
            fract_part *= 6
            converted_fract += str(int(fract_part//1))
            fract_part = fract_part%1
            k += 1
        converted_num += '.' + converted_fract
    
    if check:
        converted_num = "-" + converted_num

    return converted_num

def six_to_decimal(num):
    if num[0] == '-':
        check = True
        num = num[1:]
    else:
        check = False

    num = float(num)
    int_part = int(num//1)
    fract_part = float(num)%1

    exp = 0
    int_part = str(int_part)[::-1]
    converted_num = 0
    for i in range(len(int_part)):
        converted_num += int(int_part[i])*6**exp
        exp += 1

    if fract_part != 0:
        exp = -1
        fract_part = str(fract_part)[2:]
        for i in range(len(fract_part)):
            converted_num += int(fract_part[i])*6**exp
            exp -= 1

    if check:
        converted_num = "-" + str(converted_num)

    return str(converted_num)
