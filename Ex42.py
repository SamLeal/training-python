print('*' * 54)
print('-------\033[30mCondição de existência de um triângulo\033[0m -------')
print('*' * 54)

r1 = float(input('Informe o comprimento da 1ª reta: '))
r2 = float(input('Informe o comprimento da 2ª reta: '))
r3 = float(input('Informe o comprimento da 3ª reta: '))

sit_1 = ((r2 - r3) < r1 < (r2 + r3))
sit_2 = ((r1 - r3) < r2 < (r1 + r3))
sit_3 = ((r1 - r2) < r3 < (r1 + r2))

if (sit_1 and sit_2 and sit_3):
    print('PARABÉNS! É possível formar um triângulo com essas retas!')
    if r1 == r2 == r3:
        print('Será formado um triângulo \033[32mEQUILÁTERO\033[m!!!')
    elif r1 != r2 != r3 and r1 != r3:
        print('Será formado um triângulo \033[32mESCALENO\033[m!!!')
    else:
        print('Será formado um triângulo \033[32mISÓSCELES\033[m')
else:
    print('\033[31mDESCULPA. Não é possível formar um triângulo com essas retas.')
