nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
media = (nota1 + nota2) /2
print(f'tirando {nota1 :.1f} e {nota2 :.1f} a média do aluno é {media :.1f}')
if 7 > media >= 5:
    print('o aluno está e, RECUPERAÇÃO')
elif media < 5:
    print('a aluno está REPROVADO')
elif media >= 7:
    print('o aluno está APROVADO !!')