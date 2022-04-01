print('\033[30m*'*50)
print('{}\033[34m10 TERMOS DE UMA PA'.format(' '*15))
print('\033[30m*'*50)

a1 = float(input('Qual o primeiro termo da PA:'))
r = float(input('Qual a razão da PA:'))

for n in range(1, 11):
    posi = a1 + (n - 1) * r
    print('{:.0f}'.format(posi), end = ' ➛ ')
print('FIM')
