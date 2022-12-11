palavra = str(input('digite uma frase: '))
palavra_tratada = palavra.replace(' ', '')
if str(palavra_tratada) == str(palavra_tratada)[::-1]:
    print('palindrome')
else:
    print('não palindrome')