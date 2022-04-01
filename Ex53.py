frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ""

print('Você digitou a frase "{}"'.format(junto))

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
     print('Temos um palíndromo')
else:
     print('A frase não é um palíndromo')
