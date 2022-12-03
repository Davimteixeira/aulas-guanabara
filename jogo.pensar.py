import  random
aleatorio  = random.randint(0,6)
usuario = int(input('escreva seu numero abaixo: \n'))
if usuario == aleatorio:
    print('voce venceu')
else:
    print('voce perdeu')