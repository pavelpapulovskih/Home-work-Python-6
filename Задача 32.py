range_min = int(input("Введите минимальное значение диапазона: "))
range_max = int(input("Введите максимальное значение диапазона: "))

my_list = [2, 5, 4, 7, 1, 8, 3]
result = []

for i in range(len(my_list)):
    if range_min <= my_list[i] <= range_max:
        result.append(i)

print("Индексы элементов, удовлетворяющих условию:", result)