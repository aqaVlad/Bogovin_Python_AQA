# 2. Составить алгоритм: если введенное имя совпадает с Вячеслав,
# то вывести “Привет, Вячеслав”, если нет, то вывести "Нет такого имени"

name = input("Введите имя:  ")
if name == "Вячеслав":
    print(f"Привет, {name}")
else:
    print("Нет такого имени")
