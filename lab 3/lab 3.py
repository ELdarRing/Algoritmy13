# Задание 1
x = int(input())
if x > 0:
    print("Положительное число", x)

# Задание 2
x = int(input())
if x % 2 == 0:
    print("Четное")
else:
    print("Нечетное")
    
# Задание 3
x = int(input())

if 90 <= x <= 100:
    print("A")
elif 75 <= x <= 89:
    print("B")
elif 60 <= x <= 74:
    print("C")
else:
    print("D")

# Задание 4
age = int(input())
student = input()

if age < 18 or student.lower() == "да":
    print("имеет право")
else:
    print("не имеет")

# Задание 5
a = int(input())
b = int(input())

if a > b:
    print("Первое больше второго")
else:
    if a < b:
        print("Второе больше первого")
    else:
        print("равны")


