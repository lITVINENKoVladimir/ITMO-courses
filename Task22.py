#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.
def count_vowels(filename):

 vowel_counts = {}
 vowels = 'аеoiуиыяю'

 with open(filename, 'r') as file:
  text = file.read()
  for char in text:
   if char in vowels:
    if char in vowel_counts:
     vowel_counts[char] += 1
    else:
     vowel_counts[char] = 1

 return vowel_counts

filename = "dump.txt"

vowel_counts = count_vowels(filename)

for vowel, count in vowel_counts.items():
 print(f"Количество букв {vowel} - {count}")