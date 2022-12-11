valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um valor: '))
print('SUAS OPÇÕES ABAIXO')
print('''---------- MENU ----------
[1] Somar
[2] Multiplicar
[3] Maior
[4] novos números
[5] Saior do programa''')
resposta = 0
while resposta != 5:
    print('SUAS OPÇÕES ABAIXO')
    print('''---------- MENU ----------
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] novos números
    [5] Saior do programa''')
    print('='*40)
    resposta = int(input('Digite Sua opção: '))
    if resposta == 1:
        soma = valor1 + valor2
        print(f'A soma é de {soma}')
    elif resposta == 2:
        multiplicacao = valor1 * valor2
        print(f'A multiplicação é de {multiplicacao}')
    elif resposta == 3:
        maior = 0
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'O maior valor é de {maior}')
    elif resposta == 4:
       valor1 = float(input('Digite um valor: '))
       valor2 = float(input('Digite um valor: '))
    elif resposta == 5:
        print('FINALIZANDO')
print('fim do programa')
