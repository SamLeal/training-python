
somaid = 0
mediaid = 0
maiorid = 0
nomemaior = ''
mulhermenor = 0
contmulher = 0

for pes in range(1,5):
    print('------ \033[36m{}ª PESSOA\033[m ------'.format(pes))
    nome = str(input('Qual o nome:'))
    idade = int(input('Qual a idade:'))
    sexo = str(input('Qual o sexo?[M/F]:'))
    somaid += idade
    if pes == 1 and sexo in 'Mm':
        maiorid = idade
        nomemaior = nome
    if sexo in 'Mm' and idade > maiorid:
            maiorid = idade
            nomemaior = nome
    if sexo in 'Ff' and idade < 20:
        contmulher += 1

mediaid = somaid / 4
print('A média de idade do grupo é de {:.2f} anos.'.format(mediaid))
print('O homem mais velho é {} que tem {} anos'.format(nomemaior, maiorid))
print('Nesse grupo tem {} mulheres com menos de 20 anos'.format(contmulher))

