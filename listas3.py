listanum = []
maiornum = 0
menornum = 0
for c in range(0,5):
    listanum.append(int(input(f'digite um valor paea a posição {c}: \n')))
    if c == 0:
        maiornum = menornum = listanum[c]
    else: 
        if listanum[c] > maiornum:
            maiornum = listanum[c]
        if listanum[c] <  menornum:
            menornum = listanum[c]
print('=-'* 30)
print(f'voce digitou os valores {listanum}')
print(f'o maior valor digitado foi {maiornum} nas posições ', end='')
for i, v  in enumerate(listanum):
    if v == maiornum:
        print(f'{i}...' , end= '')

print(f'\no menor valor digitador foi {menornum} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menornum:
        print(f'{i}... ', end='')