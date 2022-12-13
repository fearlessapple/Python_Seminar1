# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# not (X or Y or Z) = not X and not Y and not Z

x = bool(input('Input True or False: '))
y = bool(input('Input True or False: '))
z = bool(input('Input True or False: '))

result1 = not (x or y or z)
result2 = (not x) and (not y) and (not z)

if result1 == result2:
    print('True')
else:
    print('False')
