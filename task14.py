#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.

# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
#
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

def find_min_distances(arrange):
    index_map = {}
    min_distances = {}

    for i, num in enumerate(arrange):
        if num in index_map:
            if num in min_distances:
                min_distances[num] = min(min_distances[num], i - index_map[num])
            else:
                min_distances[num] = i - index_map[num]
        index_map[num] = i

    for num in arrange:
        if num not in min_distances:
            print(f"Для числа {num} нет минимального растояния т.к элемент в массиве один.")
        else:
            print(f"Для числа {num} минимальное растояние в массиве по индексам: {index_map[num] - min_distances[num]} и {index_map[num]}")

mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
find_min_distances(mass)