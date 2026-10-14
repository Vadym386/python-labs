import datetime
import math
import random as ran
import statistics as stat
import datetime as dat

#1

# radius = int(input("Введіть радіус круга: "))
# a, b = map(int, input('Введіть довжину двох катетів через пробіл: ').split(' '))
# things = int(input('Предметів: '))
# in_case = int(input('В упаковці: '))
#
# print(f'Площа круга: {round(math.pi * pow(radius, 2), 2)}')
# print(f'Гіпотенуза: {round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)}')
# print(f'Потрібно упаковок: {math.ceil(things / in_case)}')


#2

# n = int(input('N = '))
# if n > 0:
#     lis = []
#     for i in range(n):
#         lis.append(ran.randint(1, 12))
#     print(f'Оцінки: {lis}')
#     print(f'Max: {max(lis)}')
#     print(f'Min: {min(lis)}')
#     print(f'Середнє: {stat.mean(lis)}')
#     print(f'Медіана: {stat.median(lis)}')
#     count = 0
#     for l in lis:
#         if l >= 10:
#             count += 1
#     print(f'Оцінок 10-12: {count}')
# else:
#     print('Неможливо визначити')


#3

# a, b, c = map(int, input('Введіть дату події через тире: ').split('-'))
# event = dat.date(a, b, c)
# now = dat.date.today()
# dif = (event - now).days
# if dif > 0:
#     print(f'До події залишилося {dif} днів')
# elif dif < 0:
#     print(f'Після події пройшло {dif * (-1)} днів')
# else:
#     print('Подія відбувається сьогодні!')