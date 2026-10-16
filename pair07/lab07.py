#1

# lines = 0
# words = 0
# symbols = 0
# all_symbols = 0
# big_len = 0
# num = 0
# big_text = ''
#
# with open('text.txt', 'r', encoding = 'utf-8') as file:
#     for number, line in enumerate(file, start = 1):
#         clean_line = line.strip()
#
#         lines += 1
#         words += len(clean_line.split())
#         for c in clean_line:
#             symbols += 1
#         all_symbols += symbols
#
#         if big_len < len(clean_line):
#             big_len = len(clean_line)
#             num = number
#             big_text = clean_line
#
# print(f'Рядків: {lines}')
# print((f'Слів: {words}'))
# print(f'Символів: {all_symbols}')
# print(f'Найдовший рядок: №{num}, {big_len} символів')
# print(f'Текст: {big_text}')


#2

# search = input('Фрагмент: ').strip().lower()
# g = False
#
# with open('text.txt', 'r', encoding = 'utf-8') as file:
#     for number, line in enumerate(file, start = 1):
#         clean_line = line.strip().lower()
#
#         if search in clean_line:
#             print(f'{number}: {line.strip()}')
#             g = True
#
# if g == False:
#     print('Даний фрагмент не знайдено!')


#3

# students = []
#
# with open('students.txt', 'r', encoding = 'utf-8') as file:
#     for line in file:
#         clean_line = line.strip()
#         name, grade = clean_line.split(';')
#         grade = int(grade)
#
#         if grade > 80:
#             students.append([grade, name])
# students.sort(reverse = True)
#
# with open('result.txt', 'w', encoding = 'utf-8') as file:
#     for grade, name in students:
#         print(f'{name};{grade}', file = file)


#4

# def convert(file_name):
#     students = {}
#     with open(file_name, 'r', encoding = 'utf-8') as file:
#         for line in file:
#             name, subject, grade = line.strip().split(';')
#             grade = int(grade)
#             if name not in students:
#                 students[name] = []
#             students[name].append(grade)
#     return students
#
# def average(students):
#     finish = []
#     for name in students:
#         long = len(students[name])
#         aver = round(sum(students[name]) / long, 2)
#         finish.append([aver, name, long])
#     finish.sort(reverse = True)
#     return finish
#
# def report(finish, file_name):
#     best = finish[0][0]
#     best_n = []
#     with open(file_name, 'w', encoding = 'utf-8') as file:
#         for average, name, long in finish:
#             print(f'{name} - оцінок: {long} - середній: {average}', file = file)
#             if average == best:
#                 best_n.append(name)
#         print(f'Найкращий результат: {' та '.join(best_n)} - {best}', file = file)
#
# conv = convert('grades.csv')
# av = average(conv)
# report(av, 'report.txt')