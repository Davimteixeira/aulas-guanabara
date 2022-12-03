nome = str(input('qual o seu nome ?: \n'))
if nome =='Davi':
   print('que nome bonito')
   print('tenha um bom dia, {}'.format(nome))
elif nome == 'pedro' or nome == 'maria'or nome == 'paulo':
    print('seu nome é popular')
elif nome in 'ana claudia jessica juliana' :
    print('seu nome é feminino')
else:
    print('não gostei')
