from datetime import date

atual = date.today().year
cont = 0
cont2 = 0

for ano in range(1,8):
    data = int(input('Qual seu ano de nascimento?'))
    idade = atual - data
    if idade >= 18:
        cont += 1
    else:
        cont2 += 1

print('Tem {} pessoas na  maioridade e {} menores.'.format(cont, cont2))
