maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('peso da {} pessoa:'.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior: 
            maior = peso
        if peso     < menor:
            menor = peso
print('o maoir peso lido foi de {}kg'.format(maior))
print('o menor peso lido foi de {}kg'.format(menor))
