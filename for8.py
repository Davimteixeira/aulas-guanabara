from datetime import date 
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1,8):
    nascimento = int(input('digite seu ano de nascimento, {} pessoa: \n'.format(c)))
    idade = atual - nascimento
    if idade >= 18:
        totalmaior += 1
    else:
       totalmenor += 1
print('ao todo tivemos {} pessoas de maiores de idade'.format(totalmaior))
print('e tambem tivemos {} pessoas de menor'.format(totalmenor))