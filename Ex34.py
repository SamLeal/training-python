sal = float(input('Qual o seu salário?'))

if sal > 1250:
    new = sal*110/100
else:
    new  = sal*115/100

print('\033[4;32mO seu salário de R${:.2f} com o aumento é de {:.2f}\033[m'.format(sal, new))