# todo: Шифр Цезаря
def caesar_shift(text, shift):


 result = ''
 for char in text:
  if char.isalpha() and char.islower():
   start = ord('а')
   shifted_char = chr((ord(char) - start + shift) % 32 + start)
  elif char.isalpha() and char.isupper():
   start = ord('А')
   shifted_char = chr((ord(char) - start + shift) % 32 + start)
  else:
   shifted_char = char
  result += shifted_char
 return result

def encrypt_file(filename):


 with open(filename, 'r') as file:
  lines = file.readlines()

 for i, line in enumerate(lines):
  shift = i + 1
  encrypted_line = caesar_shift(line.strip(), shift)
  print(f"Зашифрованная строка {i + 1}: {encrypted_line}")

# Шифрование файла
filename = 'message.txt'
encrypt_file(filename)