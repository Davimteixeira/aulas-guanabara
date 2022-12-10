from datetime import datetime
ano_nascimento = int(input('digite seu ano de nascimento: '))
ano_atual = int(datetime.today().strftime('%Y'))
idade = ano_atual - ano_nascimento
if idade < 18:
    print('Você ainda vai se alistar no exercito')
    print(f'falta {18 - idade} anos, para se alistar')
elif idade == 18:
    print('ja esta na hora de se alistar')
else:
    print('ja passou o tempo de se alistar !!!')
    print(f'ja passou {idade - 18} anos para se alistar')