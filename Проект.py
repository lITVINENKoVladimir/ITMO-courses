import random
import pickle
import time
import os
import functools

class GameData:
    def __init__(self, word, description, field, attempts, save_slot):
        self.word = word
        self.description = description
        self.field = field
        self.attempts = attempts
        self.save_slot = save_slot

    def save(self, filename="save_game_{}.dat"):
        filepath = filename.format(self.save_slot)
        with open(filepath, "wb") as f:
            pickle.dump(self.__dict__, f)
        print(f"Игра сохранена в слот {self.save_slot}!")

    @classmethod
    def load(cls, filename="save_game_{}.dat", slot=None):
        if slot is None:
            save_files = [f for f in os.listdir() if f.startswith("save_game_") and f.endswith(".dat")]
            if not save_files:
                print("Сохраненных игр не найдено.")
                return None
            print(" Доступные сохранения:")
            for i, file in enumerate(save_files):
                print(f"{i+1}. {file}")
            while True:
                try:
                    slot = int(input("Выберите номер сохранения: ")) - 1
                    if 0 <= slot < len(save_files):
                        break
                    else:
                        print("Неверный номер сохранения.")
                except ValueError:
                    print("Введите число.")
            filename = save_files[slot]

        try:
            filepath = filename if filename.startswith("save_game_") else "save_game_{}.dat".format(filename)
            with open(filepath, "rb") as f:
                data = pickle.load(f)
            return cls(**data)
        except (FileNotFoundError, EOFError):
            print("Ошибка загрузки игры.")
            return None


class Word:
    def __init__(self, word, description):
        self.word = word
        self.description = description

    def get_field(self):
        return ['_'] * len(self.word)


class Game:
    def __init__(self, words_data):
        self.words_data = words_data
        self.game_data = None

    def start_new_game(self):
        while True:
            try:
                save_slot = int(input("Выберите слот для сохранения (1-3): "))
                if 1 <= save_slot <= 3:
                    break
                else:
                    print("Неверный номер слота.")
            except ValueError:
                print("Введите число.")
        word_data = random.choice(self.words_data)

        self.game_data = GameData(word_data.word, word_data.description, word_data.get_field(), 10, save_slot)

    def load_game(self):
        self.game_data = GameData.load()

    def play(self):
        if self.game_data is None:
            print("Начните новую игру или загрузите сохраненную.")
            return

        while self.game_data.attempts > 0 and '_' in self.game_data.field:
            start_time = time.time()
            print(self.game_data.description)
            print(" ".join(self.game_data.field))
            print(f"У вас осталось {self.game_data.attempts} попыток!")

            letter = input("Введите букву: ").lower()
            if letter in self.game_data.word.lower():
                for i in range(len(self.game_data.word)):
                    if self.game_data.word[i].lower() == letter:
                        self.game_data.field[i] = self.game_data.word[i]
            else:
                self.game_data.attempts -= 1
                print("Нет такой буквы.")
            end_time = time.time()
            print(f"Ход занял {end_time - start_time:.4f} секунд")

            save_choice = input("Сохранить игру? (да/нет): ").lower()
            if save_choice == "да":
                self.save_game()

        if '_' in self.game_data.field:
            print("Вы проиграли!")
        else:
            print("Вы победили!")
            print(f"Загаданное слово: {self.game_data.word}")

    def save_game(self):
        if self.game_data:
            self.game_data.save()
        else:
            print("Нет активной игры для сохранения.")


# Пример использования:
words_data = [Word("оператор", "Это слово обозначает наименьшую автономную часть языка программирования"),
              Word("конструкция", "Это слово обозначает способ построения чего-либо"),
              Word("объект", "Это слово обозначает нечто, что имеет свойства и методы")]

game = Game(words_data)

while True:
    print("\nМеню:")
    print("1. Новая игра")
    print("2. Загрузить игру")
    print("3. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        game.start_new_game()
        game.play()
    elif choice == '2':
        game.load_game()
        if game.game_data:
            game.play()
    elif choice == '3':
        break
    else:
        print("Некорректный выбор.")