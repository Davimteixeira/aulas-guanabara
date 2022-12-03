n1 = float(input('digite a primeira nota:\n'))
n2 = float(input('digite a segunda nota;\n'))
m = (n1 + n2)/2
print('a sua média foi {:1f}'.format(m)) 
if m >= 6.0:
    print('sua media foi boa! PARABÉNS!')
else:
    print('a sua média foi ruim! ESTUDE MAIS')