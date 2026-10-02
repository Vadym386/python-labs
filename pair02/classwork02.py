# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
#ітерація - одне виконанння тіла циклу
# for i in range(1, 11, 2): # кожну другу пропускаємо
    # i = i + 1; i += 1 (інкремент - збільшення на 1; декремент - зменшення на 1)
    # print(i)

# for i in range(10, 0, -1):
#    print(i)

# for i in range(5):
#     i = i + 1
#     print(i)

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# suma = 0
# n = int(input())
# for i in range(1, n + 1):
#     suma += i
# print(suma)
#

# f = 1
# n = int(input())
# for i in range(1, n + 1):
#     f *= i
# print(f)

# n = int(input())
# count = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         count += 1
# print(count)

# while True:
#     n = int(input('введи число, для вихлду введи - 0'))
#     if n == 0:
#         break
#     print(n)

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)

# n = 876763575
# suma = 0
# while n > 0:
#     digit = n % 10
#     suma += digit
#     n = n // 10
# print(suma)

# n = 987856
# max_digit = 0
# while n > 0:
#     digit = n % 10
#     if digit > max_digit:
#         max_digit = digit
#     n = n // 10
# print(max_digit)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# ********
# ********
# ********
# ********

# width = 8
# height = 4
# for row in range(height):
#     for col in range(width):
#         print("*", end="")
#     print()