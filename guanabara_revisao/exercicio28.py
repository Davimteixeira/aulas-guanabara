import random
numero_aleatorio = random.randint(0, 6)
usuario = int(input('digite um numero entre 0 e 5: '))
if usuario == numero_aleatorio:
    print('você acertou, parabéns')
    print(f'o numero aleatório era {numero_aleatorio}')
else:
    print('voce errou')
    print(f'o numero aleatório era {numero_aleatorio}')