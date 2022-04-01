nome = str(input('Qual o seu nome:')).strip()
print('Analisando o seu nome...')

dividido = nome.split()
primeiro = dividido[0]
total = dividido

print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(primeiro, len(primeiro)))
