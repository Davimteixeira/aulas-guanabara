distancia = int(input('qual a distancia da sua viagem ? '))
if distancia <= 200:
    passagem  = distancia * 0.50
    print(f'sua passagem é de {passagem}')
else:
    passagem = distancia * 0.45
    print(f'sua passagem é de {passagem}')