# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

n = int(input('Input day of the week: '))
print(f'{n} -> ', end=' ')

if n == 6 or n == 7:
    print('YES')
elif n > 7 or n < 1:
    print('Input error.')
else:
    print('NO')
