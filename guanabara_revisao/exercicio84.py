temporaria = []
principal = []
maior = menor = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
            
    principal.append(temporaria[:])
    temporaria.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
         break
print('-=' *30)
print(f'Ao todo, voce cadrastrou {len(print)} pessoas')
print(f'O maior peso foi de {maior} kg. peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menorr peso foi de {menor} kg. peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()