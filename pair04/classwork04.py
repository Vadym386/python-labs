# колекції - структури даних,

# які дозволяють зберігати в собі набори значень
import numbers

#list - список - впорядкована змінна колекція
# grades = [12, 4, '6', 9]
# numbers = []
# numbers2 = list() #пустий список
# print(grades[2])
# # print(grades[5])
# print(len(grades))
# print(len[(grades) - 1])
# grades[2] = 6
# print(grades)

# numbers.append(5) #додається в кінець
# numbers.append(6)
# numbers.append('6')
# print(numbers)
#
# numbers.insert(1, 2)
# print(numbers)
#
# numbers.extend([5, 6, 5, '4']) #в кінець списка
# print(numbers)
#
# numbers.remove(5)
# if '6' in numbers:
#     numbers.remove('6')
# print(numbers)
#
# numbers.pop(-1)
# print(numbers)
#
# # del numbers
#
# # numbers.clear() #очистити список, він порожній
#
# print(numbers.count(5)) #скільки п'ятірок
# print(numbers.count(6))
#
# print(numbers.index(6)) #який індекс шестірки
#
# print(2 in numbers) #чи є в нас двійка?
# len() #довжина
# print(min('a', 'b'))
# max()
# sum()
# if len(numbers) > 0:
#     average = sum(numbers) / len(numbers)
#
# numbers.sort() #зростаюче
# print(numbers)
# print(numbers.sort(reverse = True)) #спадаюче
# print(numbers)
# print(sorted.numbers) # не перезаписує
#
# numbers.reverse() #дзеркально відображає список, перезаписує
#
# print(numbers[1:3])
# print(numbers[::-1])
# print(numbers[::2])

# for number in numbers:
#     print(number)

# digits = [-1, 0, 4, -5, 3, -6]
# dodatni = []
# parni = []
# for digit in digits:
#     if digit > 0:
#         dodatni.append(digit)
#     if digit % 2 == 0:
#         parni.append(digit)
# print(dodatni)
# print(parni)



# tuple - кортеж
#впорядкована незмінна колекція

# rgb  = (255, 0, 0)
# r, g, b = rgb
# print(r, g, b)
#
# data = ()
# a = (1,)
# print(a)
# #індексіція така ж як в списку
# #rgb[1] = 255

# point = (4, -6)
# point = point + (4,)
# print(point)
# a = (30, 40)
# b = (50, 60)
# c = a + b
# c = a[:1] + b[::]
# print(c)
#
# c.count()
# c.index()
# len()



# set - множина
#послідовність унікальних елементів
#
# subjects = {'CSS', 'HTML',  'Python', 'Java', 'Ruby', 'Python'}
# print(subjects)
# data = {}
# print(type(data))
# data2 = set()
# print(type(data2))
#
# data2.add('Python', 'CSS', 'Java')
#
# # data2.remove('CSS')
# data2.discard('CSS')
# deleted = data2.pop()
# #clear()
# if 'Python' in data2:
#     print('Python')
# print(data2)

# names = ['Ivan', 'Vadym', 'Ivan']
# new_names = set(names)
# print(new_names)

# names1 = {'Ivan', 'Vadym', 'Olha'}
# names2 = {'Lola', 'Vadym', 'Vila'}
# names3 = names1 | names2 #обєднання
# names4 = names1 & names2 #перетин
# names5 = names1 - names2 #віднімання
# names6 = names2 - names1
#
# print(names3)
# print(names4)
# print(names5)
# print(names6)

# dict - словники
#послідовність яка складається з пари значень (ключ і значення)

# products = ['bread', 'milk', 'apple', 'banana']
# prices = [30, 50, 50, 80]

# prices = {
#     'apple': 50,
#     'banana': 70,
#     'milk': 50,
#     'bread': 30
# }
# print(prices)
# student = {}
# student2 = dict()
#
# prices['tea'] = 75
# prices['bread'] = 35
#
# prices.update(
#     {
#         'juice': 50,
#         'coffee': 70
#     }
# )

# deleted = prices.pop('milk')
# del prices['milk']
# clear()

# .get() #вибрати результат
# .value() #отримати значення
# .items()#значення і ключ
# .key() #значення ключа

# for key, value in prices.items():
#     print(key)
#     print(value)
# print(prices)