total_gasto = 0
produtos_mil =0
produto_mais_barato =0 
while True:
    print("#"* 40)
    print('----------ATACADO DOS PRODUTOS----------')
    print("#"* 40)
    nome = str(input('Nome produto: ')).strip
    preco = float(input('Digite o valor: '))
    if preco > 0:
        total_gasto += + preco
    if preco > 1000:
        produtos_mil += 1
    if preco > 1:
        produto_mais_barato = preco
        if preco < produto_mais_barato:
           produto_mais_barato = preco
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
         break
print(f'o total gasto em compras foi de {total_gasto}')
print(f'ao todo {produtos_mil} passaram de mil reais')
print(f'o produto mais barato foi o {produto_mais_barato}')
        
total = totmil = menor = cont = 0
barato = ''
while True:
    produto =str(input("Nome do produto: "))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
         break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total de compras foi de R${total:.2f}')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')