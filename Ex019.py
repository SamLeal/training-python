from random import choice
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
dic = [a1, a1, a3, a4]
id = choice(dic)
print('O aluno sorteado foi: {}'.format(id))
