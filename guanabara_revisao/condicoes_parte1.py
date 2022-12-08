# a parte 1 vai falar sobre if e else, if = se, else= senão
tempo =  int(input('digite a idade do seu carro: '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
    
# condição simplificada
tempo =  int(input('digite a idade do seu carro: '))
print('carro novo'if tempo <= 3 else 'carro velho')

nome = str(input('qual é seu nome: ')).title()
if nome == "Davi":
    print('Que nome incrivel')
else:
    print('eita nome show')
print(f'bom dia, {nome}')

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2) /2
if media >= 6:
    print('a sua média foi boa PARABÉNS')
else:
    print('sua média não foi boa, estude mais')
print(f'a sua primeira nota é {nota1}, a sua segunda nota é {nota2}, a sua média é {media}')