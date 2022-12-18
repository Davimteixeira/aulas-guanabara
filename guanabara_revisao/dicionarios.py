pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade' : 22}
print(pessoas['idade'])
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k,v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
pessoas['nome'] = 'leandro'
pessoas['peso'] = 98.5
print(pessoas)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla':'sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['sigla'])

estado3 = {}
brasil1 = []

for c in range(0,3):
    estado3['uf'] = str(input('UNIDADE FEDERATIVA: '))
    estado3['sigla'] = str(input('SIGLA DO ESTADO: '))
    brasil1.append(estado3.copy())
for e in brasil1:
    print(e)
 