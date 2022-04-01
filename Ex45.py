from random import randint

print('\033[30m*'*50)
print('{}\033[34mPEDRA, PAPEL, TESOURA'.format(' '*14))
print('\033[30m*'*50)

itens = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
print('Pressione:\n[0] Pedra\n[1] Papel\n[2] Tesoura')
user = int(input('Escolha:'))
print('O computador jogou {}'.format(itens[comp]))

if user < 3:
    print("Você jogou {}".format(itens[user]))
    if comp == 0:
        if user == 0:
            print('EMPATE!!!')
        elif user == 1:
            print('Você GANHOU!!!')
        elif user == 2:
            print('Você PERDEU!!!')
    elif comp == 1:
        if user == 0:
            print('Você PERDEU!!!')
        elif user == 1:
            print('EMPATE!!!')
        elif user == 2:
            print('Você GANHOU!!!')
    else:
        if user == 0:
            print('Você GANHOU!!!')
        elif user == 1:
            print('Você PERDEU!!!')
        elif user == 2:
            print('EMPATE!!!')
else:
    print('\033[31mEstá não é uma opção.\033[m')
