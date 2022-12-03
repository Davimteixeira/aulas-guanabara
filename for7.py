num = int(input('digite um numero: \n'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi disivisel {} vezes'.format(num, tot))
if tot == 2:
    print('e por isso ele é PRIMO!')
else:
    print('e por isso ele NÃO é primo')