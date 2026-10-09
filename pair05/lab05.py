#1

# def rectangle(width, height):
#     return width * height
# def circle(radius):
#     return round(radius ** 2 * 3.14159, 2)
# def triangle(side, length):
#     return side * length / 2
#
# def main(figure_):
#     if figure_ == 'прямокутник':
#         width_, height_ = map(float, input('Введіть ширину та довжину через пробіл: ').strip().split(' '))
#         print(f'Площа прямокутника: {rectangle(width_, height_)} см2')
#     elif figure_ == 'круг':
#         radius_ = float(input('Введіть радіус: '))
#         print(f'Площа круга: {circle(radius_)} см2')
#     elif figure_ == 'трикутник':
#         side_, length_ = map(float, input('Введіть сторону та висоту через пробіл: ').strip().split(' '))
#         print(f'Площа трикутника: {triangle(side_, length_)} см2')
#
# figure = input('Введіть фігуру (прямокутник, круг, трикутник): ').strip().lower()
#
# main(figure)


#2

# def is_prime(n):
#     if n == 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
#
# def divisors(n):
#     divisor = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             divisor.append(i)
#     return divisor
#
# def digit_sum(n):
#     suma = 0
#     n = str(n)
#     for l in n:
#         v = int(l)
#         suma += v
#     return suma
#
# def main(number):
#     if is_prime(number) == True:
#         print('Просте число: так')
#     else:
#         print('Просте число: ні')
#     print(f'Дільники: {divisors(number)}')
#     print(f'Сума цифр: {digit_sum(number)}')
#
# num = int(input('Введіть натуральне число: '))
# main(num)


#3

# def average(grades):
#     return sum(grades) / len(grades)
#
# def minimum(grades):
#     return min(grades)
#
# def maximum(grades):
#     return max(grades)
#
# def count_above(grades, value):
#     count = 0
#     for g in grades:
#         if g > value:
#             count += 1
#     return count
#
# def main(grade, value_):
#     print(f'Середній бал: {average(grade)}')
#     print(f'Мінімальна: {minimum(grade)}')
#     print(f'Максимальне: {maximum(grade)}')
#     print(f'Вище {value_}: {count_above(grade, value_)}')
#
# numbers = list(map(int, input('Введіть оцінки через пробіл: ').strip().split(' ')))
# above = int(input('Поріг: ').strip())
# main(numbers, above)


#4

# def long(n):
#     if len(n) >= 8:
#         return True
#     else:
#         return False
#
# def cifra(n):
#     for c in n:
#         if c.isdigit() == True:
#             return True
#         else:
#             continue
#     return False
#
# def great(n):
#     for c in n:
#         if c.isupper() == True:
#             return True
#         else:
#             continue
#     return False
#
# def small(n):
#     for c in n:
#         if c.islower() == True:
#             return True
#         else:
#             continue
#     return False
#
# def special(n):
#     for c in n:
#         if c.isalnum() == False:
#             return True
#         else:
#             continue
#     return False
#
# def validate_password(password):
#     if long(password) == False:
#         print('Пароль не відповідає вимогам')
#         print('Пароль повинен містити більше 8 символів')
#         return False
#     if cifra(password) == False:
#         print('Пароль не відповідає вимогам')
#         print('Пароль повинен містити цифру')
#         return False
#     if great(password) == False:
#         print('Пароль не відповідає вимогам')
#         print('Пароль повинен містити велику літеру')
#         return False
#     if small(password) == False:
#         print('Пароль не відповідає вимогам')
#         print('Пароль повинен містити маленьку літеру')
#         return False
#     if special(password) == False:
#         print('Пароль не відповідає вимогам')
#         print('Пароль повинен містити спеціальний символ')
#         return False
#
# parol = input('Введіть пароль: ').strip()
# validate_password(parol)