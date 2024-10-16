#  # todo: База данных пользователя.
# # Задан массив объектов пользователя
#
#
# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
#
# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
#
# #Затем сообщение для ввода
# Ввидите критерии поиска: 16
#
# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

def filter_users(users, sort_type, criteria):
    if sort_type == 1:  # По возрасту
        filtered_users = [user for user in users if user['age'] > criteria]
        sorted_users = sorted(filtered_users, key=lambda x: x['age'])
    elif sort_type == 2:  # По началу имени
        filtered_users = [user for user in users if user['login'].startswith(criteria)]
        sorted_users = sorted(filtered_users, key=lambda x: x['login'])
    elif sort_type == 3:  # По статусу
        filtered_users = [user for user in users if user['group'] == criteria]
        sorted_users = sorted(filtered_users, key=lambda x: x['group'])
    else:
        return []

    return sorted_users

sort_type = 1
criteria = 16
result = filter_users(users, sort_type, criteria)

for user in result:
    print(f"Пользователь: '{user['login']}' возраст {user['age']} года , группа  \"{user['group']}\"")


