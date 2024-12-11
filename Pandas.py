# Task 1
import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd', 'e'])

# Создание Series из массива без индекса
series = pd.Series(data)

print(series)

# task2
import pandas as pd
import numpy as np

dictionary = {'A': 50, 'B': 10, 'C': 80}
index = ['B', 'C', 'D', 'A']

# Создание Series из словаря с заданным индексом
series = pd.Series(dictionary, index=index)

print(series)
# task3
import pandas as pd

data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']

# Создание Series из списка с заданным индексом
series = pd.Series(data, index=index)

print(series)

# task4
import pandas as pd

dict1 = {'California': 100, 'Texas': 200, 'New York': 300, 'Florida': 400, 'Illinois': 500}
dict2 = {'California': 'aaa', 'Texas': 'bbb', 'New York': 'ccc', 'Florida': 'ddd', 'Illinois': 'eee'}

# Создание Series из словарей
series1 = pd.Series(dict1)
series2 = pd.Series(dict2)

# Создание DataFrame из Series
df = pd.DataFrame({'population': series1, 'state_code': series2})

print(df)
# task5
import pandas as pd

index = pd.Index(list('abc'))

print(index)
# task6
import pandas as pd

lst = [['Сейчас', 25], ['я', 30], ['изучаю', 26], ['Pandas', 22]]

# Создание DataFrame из 2D-списка
df = pd.DataFrame(lst, columns=['Слово', 'Длина'])

print(df)

# task7
import pandas as pd

x = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# Выбор значения с помощью .loc()
value_loc = x.loc['c']
print(f"Значение с помощью .loc(): {value_loc}")

# Выбор значения с помощью .iloc()
value_iloc = x.iloc[2]
print(f"Значение с помощью .iloc(): {value_iloc}")

# task8
import pandas as pd

data = pd.DataFrame({'area': [1, 2, 3, 4, 5], 'pop': ['aaa', 'bbb', 'ccc', 'ddd', 'eee']})

# Выбор второй и третьей строк
print("Вторая и третья строки с помощью .iloc():")
print(data.iloc[1:3])

# Выбор второго столбца
print("Второй столбец с помощью .loc():")
print(data.loc[:, 'pop'])

# Выбор значения 'bbb'
print("Значение 'bbb' с помощью .loc():")
print(data.loc[data['pop'] == 'bbb', 'pop'].iloc[0])

# task9
import pandas as pd

data = pd.DataFrame({'column_1': [35, 21, 39, 54, 59],
          'column_2': [3000, [1, 2, 3], 'Hello', True, 47.39]})

# Транспонирование DataFrame
transposed_data = data.transpose()

print(transposed_data)


