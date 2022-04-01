from datetime import date

print('\033[30m*'*50)
print('\033[36m{}ALISTAMENTO MILITAR'.format(' '*14))
print('\033[30m*'*50)

atual = date.today().year
data = int(input('Qual o seu ano de nascimento:'))
idade = (atual)-data
print('Quem nasceu en {} tem {} anos em {}.'.format(data, idade, atual))

if idade > 18:
    tempo = idade - 18
    alist = atual - tempo
    print('\033[31mJá passou seu tempo de alistamento em {} ANOS!!!'.format(tempo))
    print('Você deveria ter se ALISTADO em {}.'.format(alist))
elif idade < 18:
    tempo = 18 - idade
    alist = atual + tempo
    print('Ainda faltam {} anos para o seu alistamento.'.format(tempo))
    print('Você deve se alistar em {}.'.format(alist))
else:
    print('\033[32mESTÁ NA HORA DE SE ALISTAR!!!')
