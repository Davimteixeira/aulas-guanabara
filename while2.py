
valor1 = int(input('digite o primeiro valor: '))
valor2 = int(input('digite o segundo valor: '))
opcao = 0
while opcao != 5:
   print('------MENU------')
   print(' [1] somar \n [2] multiplicar \n [3] maior dos dois \n [4] novos numeros \n [5] sair do programa ')
   opcao = int(input('Qual é a sua opção: '))
   if opcao == 1:
       soma = valor1 + valor2
       print('a soma entre {} e {} é {}'.format(valor1, valor2, soma))
   elif opcao == 2:
       produto = valor1 * valor2
       print('o resultado do {} x {} é {}'.format(valor1,valor2,produto))    
   elif opcao == 3:
       if valor1 > valor2:
           maior = valor1
       else:
           maior = valor2
           print('entre {} e {} o maior valor é {}'.format(valor1, valor1, maior))
   elif opcao == 4:
       print('informe os numeros novamente: ')
       valor1 = int(input('primeiro valor: '))
       valor2 = int(input('segundo valor: '))
   elif opcao == 5:
       print('finalizando...')
   else:
       print('opção invalida. tente novamente')
       print('=-=' * 10)
    
print('final do programa')