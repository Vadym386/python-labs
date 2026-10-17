# if 7 > 5:
#     print('OK')

# n = int('Number')
# print(n)

# try:
#     age = int(input('age: '))
#     print('your age: ', age)
# except ValueError:
#     print('Enter normal age')

#Value Eror - коли тип операції правильний,
# а значення в цій операції визначити не можна

# try:
#     a = int(input('a: '))
#     b = int(input('b: '))
#     result = a / b
#     print(result)
# except ValueError:
#     print('a, b - повинні бути числами')
# except ZeroDivisionError:
#     print('Ділити на 0 не можна')
# finally:
#     print('програму завершено')

# while True:
#     try:
#         grade = int(input('Enter your grade: '))
#         if grade < 1 or grade > 12:
#             raise ValueError('Grade out of range')
#         print(f'Your grade is {grade}')
#         break
#     except ValueError as error_limit:
#         print(f'Error: {error_limit}')

# def int_input(massage):
#     while True:
#         try:
#             return int(input(massage))
#         except ValueError:
#             print('Please enter an integer!')
#
# n = int_input('Please enter a number: ')
# print(n)

# def input_grade():
#     while True:
#         try:
#             grade = int(input('Enter your grade: '))
#             if grade < 1 or grade > 12:
#                 raise ValueError('Impossible grade')
#             return grade
#         except ValueError as error:
#             print(error)
#
# grade = input_grade()
# print(f'Оцінка {grade} прийнята')

# price = {
#     'apple': 10,
#     'banana': 20
# }
# product = input('Enter product name: ')
# try:
#     print(price[product])
# except KeyError:
#     print('Product not found')
#
# product = input('Enter product name: ')
# price = price.get(product, 'товару немає')
# print(price)

# try:
#     with open('data.txt','r', encoding = 'utf-8') as file:
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print('Такого файлу немає')

# line = 'Ivan;95'
# parts = line.strip().split(',')
# if len(parts) != 2:
#     print('Помилка у рядку')
# else:
#     name = parts[0]
#     grade = parts[1]
#
#     try:
#         grade_int = int(grade)
#
#         if grade_int < 0 or grade_int > 100:
#             raise ValueError('Бал не від 1 до 100')
#     except ValueError as e:
#         print(f'Помилка {e}')
#     else:
#         print(f'Правильний запис {name} - {grade_int}')

# lines = [
#     'Ivan;95',
#     'Lisa;hello',
#     'Vadym;100'
# ]
# for line_number, line in enumerate(lines, start = 1):
#     parts = line.strip().split(';')
#     if len(parts) != 2:
#         print(f'Рядок {line_number} має помилку')
#         continue
#     name = parts[0]
#     try:
#         score = int(parts[1])
#     except ValueError:
#         print(f'Рядок  {line_number}  пропущено, бал виставлений не правильно')
#         continue
#     print(f'Правильний запис {name} - {score}')