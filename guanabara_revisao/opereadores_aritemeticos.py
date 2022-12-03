n1 = int(input('um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
exponenciacao = n1 ** n2
print(f'A soma é {soma},\na multiplicacao é {multiplicacao},\ne a divisão é {divisao :.3f}\n', end=" ")
print(f'A divisão inteira é {divisao_inteira}\ne potencia {exponenciacao}')
# o \n é pra quebrar linha, e o end="" e para não quebrar a linhas nos print