# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".

def is_palindrome(number):
  """Checks if a four-digit number is a palindrome."""

number = int(input("Enter a four-digit number: "))

if 1000 <= number <= 9999:
    if is_palindrome(number):
        print("The statement is true.")
    else:
        print("The statement is false.")
else:
    print("Invalid input. Please enter a four-digit number.")