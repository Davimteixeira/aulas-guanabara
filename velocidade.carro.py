velocidade = float(input('digite a velocidade do carro:\n'))
if velocidade > 80 :
    print('carro foi multado')
    multa = (velocidade - 80) * 7
    print('voce deve pagar uma multa de r$ {:.2f}!'.format(multa))
else:
    print('voce está no limite certo')
    
