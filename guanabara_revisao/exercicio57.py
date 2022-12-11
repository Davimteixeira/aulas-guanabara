sexo = str(input("informe seu sexo: [M/F]")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados ivalidos. por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado om sucesso')

