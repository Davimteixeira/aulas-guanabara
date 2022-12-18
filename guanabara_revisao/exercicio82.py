lista = []
lista_pares = []
lista_impars = []
while True:
    usario = int(input('Digite um numero: '))
    lista.append(usario)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
         break
for n in lista:
        if n % 2 == 0:
            lista_pares.append(n)
        if n % 2 == 1:
            lista_impars.append(n)
print(lista)
print(lista_impars)
print(lista_pares)