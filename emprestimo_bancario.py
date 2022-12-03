valor_casa = float(input('Qual o valor da casa ? \n'))
salario = float(input('qual o seu salario? \n'))
tempo = int(input('em quantos anos voce vai pagar? \n'))
prestacao = valor_casa / (tempo * 12 )
minimo = salario * 30 / 100
print('para pagar uma casa de r${:.2f} em {} anos'.format(valor_casa, tempo, end=''))
print('a prestação será de r${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('emprestico pode ser CONCEDIDO')
else:
    print('emprestimo NEGADO')