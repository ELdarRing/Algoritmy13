# Задание 1
a = int(input())
b = int(input())
c = int(input())

average = (a + b + c)/ 3
print(average)

# Задание 2
x = int(input())
if x % 3 == 0 and x % 5 == 0:
    print("делится на оба числа")
else:
    print("не делится")

# Задание 3
n = int(input())
result = 1
for i in range(1, n+1):
    result *= i
print(result)


# Задание 4
n = int(input())
count = 0

for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
        count += 1

print("Четных", count)
