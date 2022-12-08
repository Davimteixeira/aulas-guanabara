velocidade_carro = int(input('Digite a velocidade do carro: '))
multa = 0
multa_dinheiro = 7.00
if velocidade_carro > 80:
    print('Voce foi multado, passou o limite de volociade')
    multa = (velocidade_carro * multa_dinheiro) - 560 
    print(f'a sua multa foi de {multa :.2f}')
else:
    print('boa viagem')
    

velocidade = float(input('digite a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO, passou o limite de velociade')
    multa1 = (velocidade-80) * 7
    print(f'a sua multa foi no valor de R$ {multa1 :.2f}')