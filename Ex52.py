num = int(input('Coloque um número:'))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
if tot == 2:
    print('O número {} é \033[32mPRIMO\033[m!!!'.format(num))
else:
    print('O número {} \033[31mNÃO\033[m é primo!!!'.format(num))
    