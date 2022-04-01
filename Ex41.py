print('\033[30m*'*50)
print('\033[34m{}CATEGORIA DO ATLETA'.format(' '*14))
print('\033[30m*'*50)

idade = int(input('Qual a sua idade:'))

if idade <= 9:
    print('Você está na categoria \033[32mMIRIM\033[m!!!')
elif 9 < idade <= 14:
    print('Você está na categoria \033[32mINFANTIL\033[m!!!')
elif 14 < idade <= 19:
    print('Você está an categoria \033[32mJUNIOR\033[m!!!')
elif idade == 20:
    print('Você está na categoria \033[32mSÊNIOR\033[m!!!')
else:
    print('VocÊ está na categoria \033[32mMASTER\033[m!!!')