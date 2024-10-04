#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

a=float(input("Enter the coefficient A:"))
b=float(input("Enter the coefficient B:"))
c=float(input("Enter the coefficient C:"))


ac=abs(c-a)
bc=abs(c-b)

sum_both= ac+bc

print(f"ac={ac}, bc={bc}, sum_both={sum_both}")