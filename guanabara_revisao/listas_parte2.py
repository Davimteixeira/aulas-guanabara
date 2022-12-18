teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'MAria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera1 = []
dado = []
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera1.append(dado[:])
    dado.clear()
print(galera1)
totmaior = 0
totmen  =0
for p in galera1:
    if p[1] >= 21:
        print(f'{p[0]} Sé maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmaior} de  maior, e temos {totmen} de menor')