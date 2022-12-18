# listas
#  listas utiliza colchetes []
# 1 =  o metodo append() ele adiciona intem na lista
# 2 = o metodo insert() ele vai adicionar um intem antes de outro item, exemplo lanche.insert(0,'cachorro_quente')
# 3 = del variavel[] ele vai apagar o indice colocado
# 4 = o metodo pop() ele remove o ultimo indice, mas se passar no parametro ele vai apagar
# o metodo remove('') ele romove mas passando o nome do indice que quer apagar
# o metodo sort() coloca os indices em ordem
# o metodo sort(reverse=True) coloca os indeces ao contrario

# pode se criar list atráves de range, exemplo : valores = list(range(4,11))
num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse= True)
num.insert(2, 2)
num.pop(2)
num.remove(2)
print(num)
print(f'essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')
valore = []
for cont in range(0,5):
    valore.append(int(input('Digite um valor: ')))

# ligando as listas
a = [2,3,4,7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# copiando as listas
c = [2,3,4,7]
d = c[:]
b[2] = 2
print(f'Lista A: {a}')
print(f'Lista B: {b}')