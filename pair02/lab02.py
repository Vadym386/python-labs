#1

# n = int(input('Введи натуральне число: '))
# suma = 0
# count = 0
# for i in range(1, n + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         suma += i
#         count += 1
# ava = suma / count
# print('Сума', suma)
# print('Кількість', count)
# print('Середнє', ava)

#2

# n = int(input())
# count = 0
# suma = 0
# maxim = 0
# minim = None
# while n > 0:
#     x = n % 10
#     y = n % 10
#     n = n // 10
#     suma += x
#     if x > maxim:
#         maxim = x
#     if minim == None:
#         minim = y
#     elif y < minim:
#         minim = y
#     count += 1
# print('Кількість цифр:', count)
# print('Сума цифр:', suma)
# print('Найбільша цифра:', maxim)
# print('Найменша цифра:', minim)

#Я тут використав None, бо я його пам'ятаю з курсів.
#По іншому я не знаю як зробити

#3

# n = int(input())
# for i in range(1, n + 1):
#     x = i
#     al = True
#     while x > 0:
#         if x % 10 == 0 or i % (x % 10) != 0:
#             al = False
#             break
#         else:
#             x = x // 10
#     if al == True:
#         print(i)
#4

# width = int(input('Ширина: '))
# height = int(input('Довжина: '))
# if width >= 3 and height >= 3:
#     for w in range(width):
#         for h in range(height):
#не знаю як робити