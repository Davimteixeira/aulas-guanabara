valor_da_casa = float(input('Digte o valor da casa: '))
salario_comprador = float(input('Digite o salario do comprador: '))
anos_pagamento = int(input('em quantos anos voce vai pagar? '))
calculo_de_anos = anos_pagamento * 12
prestacao_mensal = valor_da_casa / calculo_de_anos
nao_efutar_compra = (salario_comprador * 30) / 100
if prestacao_mensal > nao_efutar_compra:
    prestacao_mensal = print('voce não pode efetuar essa compra, seu salário não é comaptivel ao preço da casa')
elif prestacao_mensal < nao_efutar_compra:
    print('A compra pode ser feita')
    print(f'o valor da prestação mensal é de {prestacao_mensal:.2f} R$')
