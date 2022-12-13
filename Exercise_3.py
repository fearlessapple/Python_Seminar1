# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Input coordinate "X": '))
y = int(input('Input coordinate "Y": '))
print(f'x = {x}, y = {y} -> ', end=' ')

if x == 0 and y == 0:
    print('Input error.')
elif x > 0 and y > 0:
    print('First quarter')
elif x < 0 and y > 0:
    print('Second quarter')
elif x < 0 and y < 0:
    print('Third quarter')
elif x > 0 and y < 0:
    print('Fourth quarter')
elif (x == 0 and y > 0) or (x == 0 and y < 0):
    print('Axis "Y"')
else:
    print('Axis "X"')                    