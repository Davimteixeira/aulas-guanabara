# for c in range(1,10):
#     print(c)
# print('fim')

# contador = 1
# while contador < 10:
#     print(contador)
#     contador = contador + 1
# print('fim')

# for c in range(1, 2):
#     num = int(input('digite um valor: '))
# print('fim')

# n = 1
# while n != 0:
#     n = int(input('Digite um valor: '))
# print('fim')

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar: [S/N]')).upper()
# print('fim')

numero =1
par = impar = 0
while numero != 0:
    numero = int(input('digite um valor: '))
    if numero != 0:
        if numero % 2 ==0 :
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} numeros pares, e {impar} numeros impars')       
print('acabou')