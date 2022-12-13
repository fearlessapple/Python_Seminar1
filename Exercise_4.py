# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Input quarter number: "))

if quarter == 1:
    print('X ∈ (0, +∞) and Y ∈ (0, +∞)')
elif quarter == 2:
    print('X ∈ (-∞, 0) and Y ∈ (0, +∞)')
elif quarter == 3:
    print('X ∈ (-∞, 0) and Y ∈ (-∞, 0)')
elif quarter == 4:
    print('X ∈ (0, +∞) and Y ∈ (-∞, 0)')
else:
    print('Input error.')             