# ordem de precedencia
# 1 ()
# 2 **
# 3 *, /, //,, %
# 4 +, -
#  alinhamento a seguir
nome = input('qual seu nome: ')
print('Prazer em te conhecer {:20}!'.format(nome))
# alinhado em 20 caracteres
nome2 = input('Qual seu nome: ')
print('Prazer em te conhecer {:>20}!'.format(nome2))
# alinhado em a direita
nome3 = input('Qual seu nome: ')
print('Prazer em te conhecer {:<20}!'.format(nome3))
# alinhado a esquerda
nome4 = input('Qual seu nome: ')
print('Prazer em te conhecer {:^20}!'.format(nome4))
# alinhado ao centro
nome5 = input('Qual seu nome: ')
print('Prazer em te conhecer {:=^20}!'.format(nome5))
# alinhado ao centro e com = 
nome5 = input('Qual seu nome: ')
print(f'Prazer em te conhecer {nome5 :=^20}!')

