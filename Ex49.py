soma = 0
cont = 0

for um in range(1,7):
    num = int(input('Digite o {} número:'.format(um)))
    if  num %2 == 0:
        soma += num
        cont += 1

print('Você informou {} número PARES e a soma foi {}'.format(cont, soma))
