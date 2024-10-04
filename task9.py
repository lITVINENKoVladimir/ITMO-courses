A = float(input("Enter the coefficient A (A != 0): "))
B = float(input("Enter the coefficient B: "))

if A == 0:
    print("Error: Coefficient A cannot be zero.")
else:
    x = -B / A
    print("The solution to the equation is x =", x)
