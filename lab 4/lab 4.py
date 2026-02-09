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