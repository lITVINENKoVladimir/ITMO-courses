#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

# Считываем два числа
a = float(input("Write the first digit: "))
b = float(input("Write the second digit: "))

# Выполняем операции
sum_result = a + b
difference = a - b
quotient = a / b
product = a * b
integer_division = a // b
remainder = a % b
power = a ** b

# Выводим результаты
print(f"Сумма: {sum_result}")
print(f"Разность: {difference}")
print(f"Частное: {quotient}")
print(f"Произведение: {product}")
print(f"Результат целочисленного деления: {integer_division}")
print(f"Результат деления с остатком: {remainder}")
print(f"Результат возведения в степень: {power}")