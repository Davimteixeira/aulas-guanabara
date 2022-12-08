# a parte 1 vai falar sobre if e else, if = se, else= senão
tempo =  int(input('digite a idade do seu carro: '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
    
# condição simplificada
tempo =  int(input('digite a idade do seu carro: '))
print('carro novo'if tempo <= 3 else 'carro velho')