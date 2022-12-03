num1 = float(input('digite um numero: \n'))
num2 = float(input('digite o segundo numero: \n'))
if num1 > num2 :
    print(f'o {num1:.0f}, é maior que o {num2:.0f}'.format(num1, num2))
elif num2 > num1:
    print(f'o numero {num2:.0f} é maior que {num1:.0f}'.format(num2, num1))
else:
    print('os dois são iguais')