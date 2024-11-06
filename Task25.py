#todo: Взлом шифра
def caesar_decrypt(text, shift):

 result = ''
 for char in text:
  if char.isalpha():
   start = ord('A') \
       if not char.islower() else ord('a')
   decrypted_char = chr((ord(char) - start - shift) % 26 + start)
  else:
   decrypted_char = char
  result += decrypted_char
 return result

ciphertext = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

for shift in range(26):
 plaintext = caesar_decrypt(ciphertext, shift)
 print(f"Сдвиг {shift}: {plaintext}")