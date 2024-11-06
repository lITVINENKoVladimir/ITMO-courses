#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
def load_matrix(filename):

 with open(filename, 'r') as file:
  lines = file.readlines()

 matrix = [[int(x) for x in line.strip().split()] for line in lines]

 if all(len(row) == len(matrix[0]) for row in matrix):
  return matrix
 else:
  return False

filename = 'matrix.txt'
matrix = load_matrix(filename)

if matrix:
 print("Матрица:")
 for row in matrix:
  print(row)
else:
 print("Ошибка: Некорректный формат файла.")