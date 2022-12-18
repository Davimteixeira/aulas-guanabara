dicionario = {}
lista = []
dicionario['Nome'] = str(input('Digite o nome: '))
dicionario['Media'] = float(input('Digite sua média: '))
lista.append(dicionario.copy())
for k,v in dicionario.items():
    print(f'{k} = {v}')
if dicionario['Media'] >= 6:
    print('Está APROVADO')
else:
    print('está REPROVADO')