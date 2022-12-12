contador = 0
soma = 0
while True:
   numeros = int(input('Digite um numero (999 Para A Sequência): '))
   if numeros == 999:
       break
   contador += 1
   soma += + numeros
print(f'Foram digitados {contador} numeros, e a soma entre eles é de {soma}')