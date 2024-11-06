#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id - номер по порядку (от 1 до 10);
# – текст из списка algoritm
#
# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
# "EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

# Каждое значение из списка должно находится на отдельной строке.
# Выход:
# 1 % "C4.5"
# 2 % "k - means"
# и т.д.

import csv

algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori", "EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"]

with open('algoritm.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "текст из списка algoritm"])
    for i, algo in enumerate(algoritm, 1):
        writer.writerow([i, algo])