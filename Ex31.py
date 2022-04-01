dist = float(input('Qual a distancia da viagem?'))
if dist <200:
    price = dist * 0.50
else:
    price= dist * 0.45

print('\033[34mO valor total da sua viagem é de: R${:.2f}'.format(price))