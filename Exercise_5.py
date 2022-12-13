# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = float(input('Input coordinate "x1": '))
y1 = float(input('Input coordinate "y1": '))
x2 = float(input('Input coordinate "x2": '))
y2 = float(input('Input coordinate "y2": '))

delta_x = x2 - x1
delta_y = y2 - y1

import math

result = round(math.sqrt(delta_x**2 + delta_y**2), 2)
print(f'A ({x1}, {y1}); B ({x2}, {y2}) -> {result}')
