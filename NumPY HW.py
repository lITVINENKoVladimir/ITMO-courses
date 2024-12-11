# Lesson 1
# Task 1
from tkinter.ttk import Label

import numpy as np

# Создаем массив
array = np.arange(5)

print(array)

# Task 2
import numpy as np
array = np.full((3,2),1)
print(array)

# Task 3
import numpy as np
array = np.full((2,3),7)
print(array)

# Task 4
import numpy as np
array = np.full((5,2),bool(True))
print(array)

# Task 5
import numpy as np
array = np.linspace(0, 1, 5)
print(array)

# Lesson 2
# Task 1
import numpy as np
array = np.zeros((3, 2, 4))

num_dimensions = array.ndim

print("Массив:")
print(array)
print("Количество измерений:", num_dimensions)

# Task 2
import numpy as np
arr = np.array(([1,2,3]), dtype = np.int64)
print("Массив целых чисел:", arr)
print("Тип данных:", arr.dtype)

# Task 3

import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],

                [9, 10, 11, 12],

                [13, 14, 15, 16]])

odd_columns = arr[:, 0::2]
print("Элементы с нечетными столбцами:", odd_columns)

# Task 4
import numpy as np

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

submatrix = matrix[1:3, 2:4]
print(submatrix)

# Task 5

import numpy as np

tensor = np.array([[[1, 2, 3],

                    [4, 5, 6],

                    [7, 8, 9]],

                   [[10, 11, 12],

                    [13, 14, 15],

                    [16, 17, 18]],

                   [[19, 20, 21],

                    [22, 23, 24],

                    [25, 26, 27]]])
submatrix = tensor[: , :2, :2]
print(submatrix)

# Lesson 3
# Task1
import numpy as np

arr1 = np.array([[8, 8, 4],

                 [4, 2, 2],

                 [10, 10, 2]])
result_devide= arr1/2
print(result_devide)

# Task2
import numpy as np

arr1 = np.array([[1, 2, 3],

                 [4, 5, 6],

                 [7, 8, 9]])
result_double = arr1 ** 2
print(result_double)

# Task3
import numpy as np
matrix = np.array([[1, 2, 3],

                   [4, 5, 6],

                   [7, 8, 9]])
vector = np.array([0, 1, 2])
result = matrix + vector
print(result)

# Task4
import numpy as np

matrix_c = np.array([[10, 20, 30],

                     [40, 50, 60],

                     [70, 80, 90]])
matrix_d = np.array([[1, 2, 3],])

result= matrix_c - matrix_d
print(result)

# Task5
import numpy as np
matrix_e = np.array([[2, 4],

            [6, 8]])
matrix_f = np.array([[1, 2], [3,4]])
result= matrix_e * matrix_f
print(result)

# Task6
import numpy as np
array = np.array([4, 9, 16, 25])

result = np.sqrt(array)
print(result)

# Task7
import numpy as np
array = np.array([2, 4, 6, 8])
result = np.power(array, 2)
print(result)

# Task8
import numpy as np
nums_base = np.array([2, 3, 4, 5])

exponents = np.array([3, 2, 1, 4])

result = np.power(nums_base, exponents)
print(result)

# task9
import numpy as np
array1 = np.array([10, 15, 8, 20])

array2 = np.array([5, 12, 15, 10])

result = np.maximum(array1, array2)
print(result)

# Task10
import numpy as np

array1 = np.array([2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2])

result = array1 * array2

print(result)

# task11
import numpy as np
arr1 = np.array([[1, 2],

        [3, 4]])
arr2 = np.array([[5, 6],

        [7, 8]])

result = np.dot(arr1, arr2)
transposed_result = result.T
print(transposed_result)