num = int(input('Qual número:'))
for tab in range(1, 11):
    cont = num * tab
    print('{} X {:2} = {}'.format(num, tab, cont))
