from random import randint
from time import sleep
from termcolor import colored
pc = randint(0, 5)
print(colored('-=-', 'yellow') * 19)
print(colored('Vou pensar em um número entre 0 e 5. Tente adivinhar...', 'blue'))
print(colored('-=-', 'yellow') * 19)
resp = int(input('Em que número eu pensei? '))
print(colored('PROCESSANDO...', 'magenta'))
sleep(2)
if resp == pc:
    print(colored('PARABÉNS! Você conseguiu me vencer!', 'green'))
else:
    print(colored('GANHEI! Eu pensei no {} e não no {}.', 'red').format(pc, resp))