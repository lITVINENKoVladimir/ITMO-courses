# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
# x = 10
# y = 15
# z = 2
# Ответ:
# Наибольшее число 15

x = 10
y = 15
z = 2

if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z

print("Наибольшее число", largest)

# Пример:
x = 77
y = 9
z = 130
# Ответ:
# Наибольшее число 130

x = 77
y = 9
z = 130

if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z
    print("Наибольшее число", largest)