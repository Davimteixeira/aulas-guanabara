somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0 
for p in range(1,5):
    print('----------------{} PESSOA  ---------------'.format(p))
    nome = str(input('digite o nome da {} pessoa: \n'.format(p)))
    idade = int(input('digite a idade da {} pessoa: \n'.format(p)))
    sexo = str(input('digite o sexo da {} pessoa [M- masculino\n F- feminino]: \n'.format(p)))
    media = idade / 4        
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        totmulher20 += 1
        media = somaidade /4
print('a media de iadede das pessoas é de {}'.format(media))
print('o homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('ap todo são {} mulheres com menos de 20 anos'.format(totmulher20))

