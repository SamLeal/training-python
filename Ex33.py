ano = int(input('Qual o ano:'))
if ano % 4 == 0:
    print('\033[32m{} é um ano Bissexto.\033[m'.format(ano))
else:
    print('\033[31m{} não é um ano bissexto.\033[m'.format(ano))