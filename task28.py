# todo: Дописать игру "Поле чудес"
# Отгадываемые слова и описание лежат в разных массивах по одинаковому индексу.

import random
import pickle
words = ["оператор", "конструкция", "объект"]
desc_ = [ "Это слово обозначает наименьшую автономную часть языка программирования", ".." , ".." ]

# Функция для сохранения игры
def save_game(word, field, attempts, description):
  game_data = {
    "word": word,
    "field": field,
    "attempts": attempts,
    "description": description
  }
  with open("save_game.dat", "w") as f:
    pickle.dump(game_data, f)
  print("Игра сохранена!")

# Функция для загрузки игры
def load_game():
  try:
    with open("save_game.dat", "r") as f:
      game_data = pickle.load(f)
    return game_data["word"], game_data["field"], game_data["attempts"], game_data["description"]
  except FileNotFoundError:
    print("Сохраненная игра не найдена.")
    return None, None, None, None

# Начало игры
while True:
  print("1. Новая игра")
  print("2. Загрузить игру")
  print("3. Выход")
  print("4 сохранение")

  choice = input("Выберите действие: ")

  if choice == '1':
    # Выбираем слово случайным образом
    random_index = random.randint(0, len(words) - 1)
    word = words[random_index]
    description = desc_[random_index]

    # Создаем поле с "_"
    field = ['_'] * len(word)

    # Количество попыток
    attempts = 10

    # Играем
    while attempts > 0 and '_' in field:
      print(description)
      print(" ".join(field))
      print(f"У вас осталось {attempts} попыток!")

      letter = input("Введите букву: ")
      if letter in word:
        for i in range(len(word)):
          if word[i] == letter:
            field[i] = letter
      else:
        attempts -= 1
        print("Нет такой буквы.")

    # Проверяем результат
    if '_' in field:
      print("Вы проиграли!")
    else:
      print("Вы победили!")
      print(f"Загаданное слово: {word}")

  elif choice == '2':
    word, field, attempts, description = load_game()
    if word is not None:
      # Продолжаем игру с загруженных данных
      while attempts > 0 and '_' in field:
        print(description)
        print(" ".join(field))
        print(f"У вас осталось {attempts} попыток!")

        letter = input("Введите букву: ")
        if letter in word:
          for i in range(len(word)):
            if word[i] == letter:
              field[i] = letter
        else:
          attempts -= 1
          print("Нет такой буквы.")

      # Проверяем результат
      if '_' in field:
        print("Вы проиграли!")
      else:
        print("Вы победили!")
        print(f"Загаданное слово: {word}")

  elif choice == '3':
    break
  elif choice == '4': # Сохранение игры
    save_gameve_game(word, field, attempts, description)
else:
    print("Некорректный выбор.")