#todo: Модифицировать программу таким образом чтобы она выводила
#  приветствие "Hello", которое до этого записано в файл text.txt
#  через метод write()

f = open("text.txt" , "w")
f.write("Hello")

# Модификация

with open("text.txt", "r") as f:
    greeting = f.read().strip()
print(greeting)
