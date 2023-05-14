# 3. Составить алгоритм: на входе есть числовой массив,
# необходимо вывести элементы массива кратные 3

array = input("Введите числа через пробел:  ").split()
L = [int(i) for i in array]
for i in range(len(L)):
    if L[i] % 3 == 0:
        print(L[i])


array = list(map(int, input("Введите числа через пробел:  ").strip().split()))
my_list = [i for i in array if i % 3 == 0]
print(my_list)