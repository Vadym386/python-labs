#1

# def error(num1, num2, operat):
#     symbols = ['+', '-', '*', '/']
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#     except ValueError:
#         return 'Помилка: це не натуральне число'
#
#     if operat == '+':
#         return num1 + num2
#     elif operat == '-':
#         return num1 - num2
#     elif operat == '*':
#         return num1 * num2
#     elif operat == '/':
#         try:
#             return num1 / num2
#         except ZeroDivisionError:
#             return 'Помилка: на нуль ділити не можна'
#     else:
#         return 'Помилка: невідома операція'
#
# number1 = input('Перше число: ')
# number2 = input('Друге число: ')
# operation = input('Операція: ')
# print(error(number1, number2, operation))


#2

# def input_grade():
#     while True:
#         grade = input('Оцінка: ')
#         try:
#             grade = int(grade)
#         except:
#             print('Помилка: введіть ціле число')
#             continue
#         try:
#             if grade < 1 or grade > 12:
#                 raise ValueError('оцінка повинна бути від 1 до 12')
#         except ValueError as val:
#             print(f'Помилка: {val}')
#             continue
#         else:
#             print (f'Прийнято: {grade}')
#             break
#
# input_grade()


#3

# def safe(n):
#     students = ['Vadym', 'Ivan', 'Olha', 'Anna']
#     sub_grade = {
#         'math': '10',
#         'literature': '8',
#         'PY': '11',
#         'physics': '7'
#     }
#     if n == '1':
#         try:
#             index = int(input('Індекс: '))
#             return students[index]
#         except ValueError:
#             return 'Введіть ціле число'
#         except IndexError:
#             return 'Індекс не знайдено'
#     elif n == '2':
#         try:
#             subject = input('Введіть предмет: ')
#             return sub_grade[subject]
#         except KeyError:
#             return 'Предмет не знайдено'
#     else:
#         return 'Введіть 1 або 2'
#
# number = input('Введіть 1 - учень, 2 - предмет: ')
# print(safe(number))


#4

# def res(file_name):
#     error_count = 0
#     count = 0
#     students = {}
#     try:
#         with open(file_name, 'r', encoding = 'utf-8') as file:
#             for number, line in enumerate(file, start = 1):
#                 count += 1
#                 c_line = line.strip()
#                 try:
#                     part = c_line.split(';')
#                     name = part[0]
#                     grade = part[1]
#                     if len(part) != 2:
#                         raise IndexError('рядок записаний не правильно')
#                     grade = int(grade)
#                     if grade < 0 or grade > 100:
#                         raise KeyError('бал поза діапазоном')
#                     students[grade] = name
#                 except IndexError as ind:
#                     error_count += 1
#                     print(f'Рядок {number} пропущено: {ind}')
#                     continue
#                 except ValueError:
#                     error_count += 1
#                     print(f'Рядок {number} пропущено: бал не є числом')
#                     continue
#                 except KeyError as ke:
#                     error_count += 1
#                     print(f'Рядок {number} пропущено: {ke}')
#                     continue
#         g_list = list(students.items())
#         g_list.sort(reverse = True)
#         print(f'Правильних записів: {count - error_count}')
#         print(f'Пропущено: {error_count}')
#         with open('report.txt', 'w', encoding = 'utf-8') as f:
#             for grade, name in g_list:
#                f.write(f'{name};{grade}\n')
#         print('Створено report.txt')
#     except FileNotFoundError:
#         print('Файл не знайдено')
#
# res('students.txt')