print('\033[30m*'*50)
print('\033[36m       Transformador de bases númericas!!!\033[m')
print('\033[30m*'*50)

num = int(input('Digite o número à ser transformado:'))
qual = int(input("Escolha a base de conversão:\033[m"
                 "\n [\033[32m1\033[m] Para BINÁRIO\n [\033[32m2\033[m] Para OCTAL"
                 "\n [\033[32m3\033[m] Para HEXADECIMAL\n Opção: "))

if qual == 1:
    print(' O número {} em binário é {}.'.format(num, bin(num)[2:]))
elif qual == 2:
    print(' O número {} em octal é {}.'.format(num, oct(num)[2:]))
elif qual == 3:
    print(' O número {} em hexadecimal é {}.'.format(num, hex(num[2:])))
else:
    print('\033[31m   OPÇÃO INVÁLIDA!!!')

