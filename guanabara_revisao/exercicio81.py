lista = []
cont = 0
while True:
    usario = int(input('Digite um numero: '))
    lista.append(usario)
    cont += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
         break
print('-=' *40)
print(f'Foram digitados {cont} numeros')
print('-=' *40)
lista.sort(reverse=True)
print(f'a lista é: {lista}')
print('-=' *40)
print('Numero 5 está na lista ?')
if 5 in lista:
    print('Sim') 
else:
    print('Não') 
print('-=' *40)