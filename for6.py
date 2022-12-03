soma = 0
cont = 0
for numeros in range(1, 7):
    digitos = int(input('digite o {} numero: \n'.format(numeros)))
    if digitos % 2 == 0:
          soma += digitos
          cont += 1
print('voce informou {} numeros pares e a soma foi {}'.format(cont, soma))