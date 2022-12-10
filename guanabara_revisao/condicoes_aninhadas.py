nome = str(input('Qual seu nome? ')).title()
if nome == 'Gustavo':
    print('nome legal')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é popular no brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('belo nome feminino')
else:
    print('Seu nome é show')
    
print(f'Tenha um bom dia, {nome}')