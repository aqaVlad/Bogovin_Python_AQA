# 1. Составить алгоритм: если введенное число больше 7, то вывести "Привет"

number = input("Введите число:  ")
try:
    if float(number) > 7:
        print("Привет")
    else:
        print("Попробуй еще раз")
except:
    print("Это не число")
