#1

# text = input('Введітьь текст: ')
# long = len(text)
# print('Символів: ', long)
#
# liters = 0
# numbers = 0
# probils = 0
# for char in text:
#     if char.isalpha():
#         liters += 1
#     if char.isdigit():
#         numbers += 1
#     if char.isspace():
#         probils += 1
# print('Літер: ', liters)
# print('Цифр: ', numbers)
# print('Пробілів: ', probils)
#
# text_1 = text.lower()
# golosni = 'eyuioaq'
# count = 0
# for char in text_1:
#     if char in golosni:
#         count += 1
# print('Голосних: ', count)
#
# word = text.split()
# words = len(word)
# print('Слів: ', words)

#2

# name = input('Enter name: ')
# original = name.title().strip()
# okremi = original.split()
# ima = okremi[1][0]
# bat = okremi[2][0]
# pris = okremi[0][::]
# print(pris, ima + '.', bat + '.')

#3

# first = input('Впишіть перше слово: ').strip().capitalize()
# second = input('Впишіть друге слово: ').strip().capitalize()
# one = first.replace(' ', '').lower()
# two = second.replace(' ', '').lower()
# x = None
# for f in one:
#     if f in two:
#         x = True
#         continue
#     else:
#         x = False
#         break
# print(first)
# print(second)
# if x == True:
#     print('Рядки є анаграмами')
# else:
#     print('Рядки не є анаграмами')

#4

# text = input('Введіть текст: ').strip()
# words = text.split()
# unic = text.lower().split()
# long = None
# for w in words:
#     if long is None:
#         long = len(w)
#     elif len(w) > long:
#         long = len(w)
#         maxim = w
# print('Найдовше: ', maxim)
#
# long2 = None
# for a in words:
#     if long2 is None:
#         long2 = len(a)
#     elif len(a) < long2:
#         long2 = len(a)
#         minim = a
# print('Найкоротше: ', minim)
#
# count = 0
# un = ''
# for x in unic:
#     if x not in un:
#         un = un + x + ' '
#         count += 1
# print('Унікальні слова: ', count)
#
# change = input('Яке слово хочете замінити? ')
# on_change = input('На яке слово хочете замінити? ')
# last_change = text.replace(change, on_change)
# print('Після заміни: ', last_change)