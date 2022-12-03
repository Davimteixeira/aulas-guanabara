num = [2,5,9,1]
num [2] = 3  #estou mudando o elemento 2 para 3
num.append(7) #estou adicionando o 7 na lista
num.sort(reverse=True) #estou colocando a lista em oredem decrescente
num.insert(2,2) #estou inserindo no paremetro 2 o numero 0
num.pop(2) # estou removendo o numero 2
num.remove(2) # ele procura a primeira ocorrencia do elemento é remove
print(num)
print(f'essa lista tem {len(num)} elementos.') #o len() ler quantos elementos tem na lista

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}')
print('cheguei ai final da lista')