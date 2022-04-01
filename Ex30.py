num = int(input('Qual o número?'))
resposta = num % 2
if resposta == 0:
    print('\033[32mO número {} é par.\033[m'.format(num))
else:
    print('\033[31mO número {} é impar.\033[m'.format(num))