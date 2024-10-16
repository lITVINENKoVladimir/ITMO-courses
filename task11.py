# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.
print("Enter Year:")
year= int(input())
def get_century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
century = get_century(year)
print(f"{year} год соответстqвует {century} столетию.")
