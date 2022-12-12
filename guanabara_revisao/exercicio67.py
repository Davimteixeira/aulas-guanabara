while True:
    print('='*40)
    numero = int(input('Digite o numero para ser mostrado a taboada: '))
    print('='*40)
    print(f'''    {numero} x 1 = {numero * 1}
    {numero} x 2 = {numero * 2}
    {numero} x 3 = {numero * 3}
    {numero} x 4 = {numero * 4}
    {numero} X 5 = {numero * 5}
    {numero} x 6 = {numero * 6}
    {numero} x 7 = {numero * 7}
    {numero} x 8 = {numero * 8}
    {numero} x 9 = {numero * 9}
    {numero} x 10 = {numero * 10}''')
    if numero < -1 :
        break
print('TABUADA ENCERRADO. Volta sempre! ')