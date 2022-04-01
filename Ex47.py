s = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
         s += c
         contador += + 1
print('São {} números, somando o total de {}.'.format(contador, s))
