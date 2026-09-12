# прямой код для полож. числа
a = 45
bina = bin(a)[2:]
resa = '0' * (7-len(bina)) + bina
print('Прямой код положительного числа: a = 0.' + resa)


# прямой код для отриц. числа
b = -106
binb = bin(-b)[2:]
resb = '0' * (7-len(binb)) + binb
print('Прямой код отрицательного числа: b = ', '1.' + resb)

# вычитание в прямом коде
sum1 = int(resb, 2) - int(resa, 2)
sum_bin = bin(sum1)[2:]
res_sum1 = '0' * (7-len(sum_bin)) + sum_bin
print('Сумма двоичных чисел в прямом коде: 1.', res_sum1)

# обратный код для отриц. числа
invb = bin((-b))[2:]
reverse = ''
for i in invb:
    if i == '0':
        reverse += '1'
    if i == '1':
        reverse += '0'
res_rever = '0' * (7 - len(reverse)) + reverse
print('Обратный код для отрицательного числа: 1.' + res_rever)

# сложение в обратном коде
sum2 = int(res_rever, 2) + int(resa, 2)
sum_bin2 = bin(sum2)[2:]
res_sum2 = '1.' + sum_bin2
print('Сумма двоичных чисел в обратном коде: ', res_sum2)

# дополнительный код для отриц. числа
res_dop = ''
for i in res_rever[::-1]:
    if i == '1':
        res_dop +='0'
    else:
        res_dop += '1'
print('Дополнительный код: 1.' + res_dop)

# сложение в доп. коде
sum3 = int(res_dop, 2) + int(resa, 2)
sum_bin3 = bin(sum3)[2:]
res_sum3 = '1.' + '0' * (7 - len(sum_bin3)) + sum_bin3
print('Сумма двоичных чисел в дополнительном коде: ', res_sum3)
