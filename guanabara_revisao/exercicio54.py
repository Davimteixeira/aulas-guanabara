cont_maior = 0
cont_menor = 0
for c in range(0,8):
    pessoas = int(input('digite sua idade: '))
    if pessoas >= 18:
       cont_maior += + 1
    elif pessoas < 18:
       cont_menor += +1

print(f'o tanto de pessoas de maior é de {cont_maior}, o tanto de pessoas de menor é de {cont_menor}')