print('MANEIRAS DE USAR A TUPLA')
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'eu vou comer {comida}')
print('comi pra caramba')
for cont in range(0, len(lanche)):
    print(lanche[cont])
for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]}')
for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posção {pos}')
    
print(sorted(lanche))
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))
 

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.index(8))

pessoa = ('gustavo', 39, 'M', 99.98)
print(pessoa)
# del() = ele apaga uma tupla