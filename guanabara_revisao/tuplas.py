# As Tuplas são IMUTÁVEIS
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[0])
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(len(lanche))
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

for cont in range(0, len(lanche)):
    print(lanche[cont])

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} e na posição {pos}')

# esse metodo sorted() ele organiza
print(sorted(lanche))

a  = (2,5,4)
b = (5, 8,1,2)
c = b + a
# sorted() orgazina
print(sorted(c))
# len() ele conta
print(len(c))
# o count ele vai contar quantas vezes aparece um indice
print(c.count(5))
# o index() em que posição ta o indice passado nos parametros
print(c.index(2))
print(c.index(2,5))
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
# o metodo del() e para apagar
del(pessoa)
