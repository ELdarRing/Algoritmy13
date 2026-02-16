#Задание 1
n = int(input("Введите количество элементов:"))

if n <= 0:
    print("Ошибка")
else:
    numbers = []

    for i in range(n):
        value = int(input())
        numbers.append(value)

    print("Массив:", numbers)

#Задание 2
summa = 0
max1 = numbers[0]
min1 = numbers[0]

for i in range(n):
    summa += numbers[i]

    if numbers[i] > max1:
        max1 = numbers[i]

    if numbers[i] < min1:
        min1 = numbers[i]

average = summa / n

print("Сумма:", summa)
print("Максимум:", max1)
print("Минимум:", min1)
print("Среднее:", average)

#Задание 3
positive = 0
negative = 0
even = 0

for i in range(n):
    if numbers[i] > 0:
        positive += 1
    if numbers[i] < 0:
        negative += 1
    if numbers[i] % 2 == 0:
        even += 1

print("Положительных:", positive)
print("Отрицательных:", negative)
print("Чётных:", even)

#Задание 4
x = int(input())
found = False

for i in range(n):
    if numbers[i] == x:
        print("Индекс:", i)
        found = True
        break

if not found:
    print("Число не найдено.")

#Задание 5
numbers = [1, 5, 3, 9, 7, 12]
n = len(numbers)

if n < 2:
    print("Недостаточно элементов.")
else:
    first = numbers[0]
    second = numbers[0]

    for i in range(n):
        if numbers[i] > first:
            second = first
            first = numbers[i]
        elif numbers[i] > second and numbers[i] != first:
            second = numbers[i]

    if first == second:
        print("Второго по величине элемента нет.")
    else:
        print("Второй по величине:", second)
