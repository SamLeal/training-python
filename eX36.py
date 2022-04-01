print('\033[30m*'*50)
spc = ' '*15
print('\033[36m{}EMPRÉSTIMO BANCARIO'.format(spc ))
print('\033[30m*'*50)

casa = float(input('Qual o valor da casa?'))
sal = float(input('Qual o valo do salário do comrprador?'))
ano = float(input('Quantos anos de financiamento?'))
prestação = casa / (ano*12)
min = sal * (30/100)

if prestação <= min:
    print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, ano), end='')
    print(' a prestação sera de R${:.2f}'.format(prestação))
    print('\033[32mPARABÉNS!!! Empréstimo pode ser CONCEDIDO.')
else:
    print('\033[31mInfelizmente você não está apto para receber este fincanciamento.')

