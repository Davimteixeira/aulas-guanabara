# 1 = len() : ele vai contar o tamanho de uma string
# exemplo frase = 'curso em video python'
# len(frase)
# *****************************************************
# 2 = o count() : ele vai contar quantas vezes aparece a string que foi colocado no parametr
# exemplo: frase.count('o'), outro exemplo só que com limite: frase.count('o',0,13)
# *****************************************************
# 3 = o find() ele vai dizer quantas vezes foi encontrada a string passado no parametro
# exemplo: frase.finf('deo)
# *****************************************************
# 4 = o operador in ele vai funcionar tambem para encontrar algo dentro de uma variavel
# exemplo 'curso' in frase
# *****************************************************
# 5 = o replace() ele vai substituir uma string por outra string 
# exemplo: frase.replace("pyrhon", "android")
# *****************************************************
# 6 = o upper() ele vai deixar todas as letra da string em maisculo
# exemplo frase.upper()
# *****************************************************
# 7 = o lower() vai colocar as de uma string em minisculo, e as que estavam em maisculo tambem vai ficar miniscula
# exemplo: frase.lower()
# 8 = o capitalize ele vai jogar tudo para minisculo e a priemira letra ele deixa maiscula
# exemplo: frase.capitalize()
# 9 = o title() onde tiver um espaço ele vai separar por strings e vai deixar a primeira letra maiscula
# exemplo: frase.title()
# 10 = o strip() vai tirar os espaços da esquerda e da direita e mantendo os espaços do meio
# exemplo: frase.strip()
# 11 = o rstrip ele vai remover somente os espaços da direita
# exemplo = frase.rstrip()
# 12 = o lstrip() ele vai remover os espaços da esquerda 
# exemplo frase.lstrip()
# 13 = o split() onde tiver espaço ele vai criar uma divisão
# exeplo frase.split()
# 14 = o join(frase) ele vai fazer a junção das strings
# exemplo '-'.join(frase)

frase = 'curso em video python'
# fatiamento
print(frase[3])
print(frase[3:14])
print(frase[:14])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('o'))
print(len(frase))

frase1 = '   curso em video python  '
print(len(frase1.strip()))
print(frase1.strip())
print(frase1.replace('python', 'android'))
frase1 = frase1.replace('python', 'android')
print('curso' in frase1)
