#1

# numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
# dodatni = []
# videmni = []
# parni = []
# kratni = []
# for d in numbers:
#     if d > 0:
#         dodatni.append(d)
#     if d < 0:
#         videmni.append(d)
#     if d % 2 == 0:
#         parni.append(d)
#     if d % 3 == 0:
#         kratni.append(d)
# minim = min(numbers)
# maxim = max(numbers)
# suma = sum(numbers)
# average = round(sum(numbers) / len(numbers), 2)
#
# print('Додатні: ', dodatni)
# print('Від`ємні: ', videmni)
# print('Парні: ', parni)
# print('Кратні 3: ', kratni)
# print('Min: ', minim)
# print('Max: ', maxim)
# print('Sum: ', suma)
# print('Average: ', average)


#2

# group1 = {'Anna', 'Ivan', 'Olha'}
# group2 = {'Ivan', 'Maksym', 'Olha'}
# all = group1 & group2
# print('Спільні: ', all)
# only1 = group1 - group2
# print('Тільки group1: ', only1)
# only2 = group2 - group1
# print('Тільки group2: ', only2)
# whole = group1 | group2
# print('Усі: ', whole)


#3

# products = {
#     'coffee': 40,
#     'milk': 25,
#     'bread': 15,
#     'juice': 50,
#     'tea': 55
# }
#
# v = input('Enter name of product: ')
# k = int(input('Enter price of product: '))
# products[v] = k
# print(products)
#
# x = input('The product that you want to find: ')
# new_price = products.get(x)
# print(new_price)
#
# a, b = map(int, input('Enter a diapason: ').split('..'))
# for name, price in products.items():
#     if a <= price <= b:
#         print(name, '—', price, 'грн')


#4

# group_info = ('10-IT', '2026/2027')
# students = {
#     'Ivan': [7, 10, 9, 12, 8],
#     'Vadym': [11, 6, 9, 10, 8]
# }
#
# print('Додавання студента')
# name = input('Enter name of student: ')
# grades = list(map(int, input('Enter grades for student: ').split(' ')))
# students[name] = grades
#
# print('Друк щоденника')
# print(group_info[0], '—', group_info[1])
# for name, grades in students.items():
#     print(name + ':', *grades)
#
# print('Середній бал кожного студента')
# average = {}
# for name, grades in students.items():
#     aver = sum(grades) / len(grades)
#     average[name] = round(aver, 2)
#     print(name, '—', average[name])
#
# print('Рейтинг за середнім балом')
# print('НЕ ЗНАЮ ЯК ЦЕ ЗРОБИТИ')
#
# print('Найкращий студент')
# best_name = ''
# best_average = 0
# for name, grades in students.items():
#     average = sum(grades) / len(grades)
#     if average > best_average:
#         best_name = name
#         best_average = average
# print(best_name, '—', best_average)