numero1 = int(input('digite um numero: '))
numero2 = int(input('digite um numero: '))
numero3 = int(input('digite um numero: '))
if numero1 < numero2:
    menor = numero1
else:
    menor = numero2
if numero2 < numero3:
    menor = numero2
else:
    menor = numero3
if numero1 > numero2:
    maior = numero1
else:
    maior = numero2
if maior > numero3:
    maior = maior
else:
    maior = numero3

    
print(f'o maior numero é {maior}, o menor numero é {menor}')