import random
cont = 1
numero_aleatorio = random.randint(0, 6)
usuario = int(input('digite um numero entre 0 e 5: '))
while usuario != numero_aleatorio:
    usuario = int(input('digite um numero entre 0 e 5: '))
    cont += 1  
print(f'VOCÊ ACERTOU !!!!')
print(f'O seu numero aleatório era {numero_aleatorio}\nVocê fez {cont} tentativas')
