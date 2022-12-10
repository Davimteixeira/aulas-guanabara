soma = 0
for c in range(0,7):
    numeros = int(input('digite um numero: '))
    if numeros % 2 == 0:
        soma = soma + numeros
print(f'a soma dos numeros pares são {soma}')