print('\033[30m--------------\033[34mLOJA DO SAMUEL\033[30m--------------\033[m')

preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO: \n[ 1 ] à vista dinheiro/cheque'
      '\n[ 2 ] à vista cartão \n[ 3 ] 2x no cartão'
      '\n[ 4 ] 3x ou mais no cartão')
forma = int(input('Qual a opção? '))

if forma == 1:
     new = preco * 0.9
     print('A sua compra de R${} com 10% de '
           'desconto à vista é R${}'.format(preco, new))
elif forma == 2:
    new = preco * 0.95
    print('A sua compra de R${} com 5% de desconto'
          ' à vista no cartão é R${}'.format(preco, new))
elif forma == 3:
    par = int(input('Quantas parcelas?(1 ou 2): '))
    if par ==  1 or par == 2:
        parcela = preco / par
        print('Sua compra de R${} será parcelada em {}x de R${:.2f}'.format(preco, par, parcela))
    else:
        print('Estã quantidade de parcelas está \033[31mINDISPONIVEL\033[m!!!')
elif forma == 4:
    new = preco * 1.20
    par = int(input('Quantas parcelas?(3 à 18): '))
    if 3 <= par <= 18:
        parcela = new / par
        print('O preço com 20% de juros é {}'.format(new))
        print('Será pago em {}x de {}'.format(par, parcela))
    else:
        print('Estã quantidade de parcelas está \033[31mINDISPONIVEL\033[m!!!')
else:
    print('Esta \033[31mNÃO\033[m é uma opção')

