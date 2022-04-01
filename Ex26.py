frase = str(input('Escreva uma frase:')).strip().lower()

print('A letra "A" aparece {} vezez na frase.'.format(frase.count('a')))
print('Ela aparece a primeira vez na posição {}.'.format(frase.find('a') + 1))
print('Ela aparece a ultima vez na posição {}'.format(frase.rfind('a')+1))