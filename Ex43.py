print('\033[30m*'*50)
print('{}\033[34mCALCULE SEU INDÍCE DE MASSA CORPÓREA'.format(' '*7))
print('\033[30m*'*50)

peso = float(input('Qual o seu peso:'))
altura = float(input('Qual a sua altura:'))
imc = peso / (altura * altura)
print('O seu IMC é {:.2f}.'.format(imc))

if imc <= 18.5:
    print('Você está \033[31mABAIXO do peso\033[m!!!')
elif 18.5 < imc <= 25:
    print('Você está no peso \033[32mIDEAL\033[m!!!')
elif 25 < imc <= 30:
    print('Você está com \033[31mSOBREPESO\033[m!!!')
else:
    print('Você está com \033[31mOBESIDADE\033[m!!!')
