velo = float(input('Qual a velocidade do carro(km/h)?'))
if velo <= 80:
    print('Você esta no limite de velocidade.')
else:
    print('MULTADO!Você excedeu o limite de velocidade permitido que é de 80km¹h')
    multa = (velo-80)*7
    print('Sua multa está no valor de:R${:.2f}'.format(multa))