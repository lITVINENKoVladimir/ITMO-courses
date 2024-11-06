#todo: Числа в буквы
def replace_numbers_with_letters(text):

 words = text.split()
 result = []
 for word in words:
  if word.isdigit():
   letter = chr(int(word) + ord('A') - 1)
   result.append(letter)
  else:
   result.append(word)
 return ' '.join(result)

# Примеры
text1 = "8 5 12 12 15"
text2 = "8 5 12 12 15 , 0 23 15 18 12 4 !"

print(f"Input: {text1}")
print(f"Output: {replace_numbers_with_letters(text1)}")

print(f"Input: {text2}")
print(f"Output: {replace_numbers_with_letters(text2)}")