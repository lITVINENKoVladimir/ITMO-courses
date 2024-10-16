#todo: Заданы множества
# все пользователи
all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
# пользователи не в сети
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}

# Вычислить пользователей online


# #todo: Заданы множества
# #Даны читатели книг
# readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1' }
#
# #Даны читатели газет
# readers_magazines = { 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
#
# Найти пользователей кто читает и книги и газеты

# Первый пункт
online_users = all_users - offline_users
print(online_users)  # {'id5', 'id8', 'id1', 'id10'}


readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1'}
readers_magazines = {'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}

readers_both = readers_books & readers_magazines
print(readers_both)  # {'id8', 'id2', 'id1'}
