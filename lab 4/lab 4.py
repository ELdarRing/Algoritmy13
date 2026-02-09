# Задание 1
x = int()
while x <= 0:
 x = int() 
print(x)

#Задание 2
while True:
  x1 = int(input())
  if x1 > 100:
    break
print(x1)

# Задание 3
n = int(input())
total = 0

for i in range(1, n + 1):
    total += i

print(total)

# Задание 4
for i in range (1, 6):
  for j in range(1, 6):
    print(i*j)
print()
# Задание 5
i = 1
while i <= 10:
    print(i)
# цикл является бесконечным, потому что после выполнения условия с i не выполняются действия

# Доп задание
all_count = 0
positive_count = 0
negative_count = 0
all_sum = 0

print("Введите числа:")

while True:
    num = int(input())
    if num == 0:
        break

    all_count += 1
    all_sum += num

    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print("Общее количество чисел:", all_count)
print("Положительных чисел:", positive_count)
print("Отрицательных чисел:", negative_count)
print("Сумма чисел:", all_sum)

if all_count > 0:
    print("Среднее арифметическое:", all_sum / all_count)
else:
    print("Среднее арифметическое не вычисляется")


