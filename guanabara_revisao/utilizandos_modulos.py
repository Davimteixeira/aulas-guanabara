import math
numero = int(input('Digite um numero: '))
raiz = math.sqrt(numero)
# o sqrt() vai calcular a raiz
print(f'A raiz de {numero} é igual a {raiz}')
print(f'A raiz de {numero} é igual a {raiz :.2f}')
# vai arredondar para duas casas decimais 
print(f'A raiz de {numero} é igual a {math.ceil(raiz)}')
# o .cell(raiz) vai arrendodar o numero para cima
print(f'A raiz de {numero} é igual a {math.floor(raiz)}')
# o .cell(raiz) vai arrendodar o numero para baixo