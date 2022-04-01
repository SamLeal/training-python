print('\033[30m*'*50)
print('\033[36m{}Veja se você foi APROVADO!!!'.format(' '*12))
print('\033[30m*'*50)

n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1 + n2) / 2

if media < 5:
    print(' Sua média é {}.\n Você está '
          '\033[31mREPROVADO\033[30m!!!'.format(media))
elif media >= 7:
    print(' Sua média é {}\n Você está '
          '\033[32mAPROVADO\033[30m!!! '.format(media))
else:
    print(' Sua média é {}.\n Você está de '
          '\033[33mRECUPERACÃO\033[30m!!!'.format(media))
