#1

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#     def perimetr(self):
#         return 2 * (self.width + self.height)
#     def info(self):
#         print(f'{self.width}x{self.height}: площа = {self.area()}, периметр = {self.perimetr()}')
#
# rectangle1 = Rectangle(5, 3)
# rectangle2 = Rectangle(10, 4)
# rectangle1.info()
# rectangle2.info()


#2

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)
#         else:
#             return f'Оцінка {grade} не додається'
#     def average(self):
#         if len(self.grades) == 0:
#             return 'Список порожній'
#         else:
#             return round(sum(self.grades) / len(self.grades), 2)
#     def __str__(self):
#         return f'{self.name}: {self.grades}, середній = {self.average()}'

# student = Student('Ivan Petrenko')
# student.add_grade(10)
# student.add_grade(12)
# student.add_grade(15)
# student.add_grade(9)
# print(student)


#3

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)
#         else:
#             return f'Оцінка {grade} не додається'
#
#     def average(self):
#         if len(self.grades) == 0:
#             return 'Список порожній'
#         else:
#             return round(sum(self.grades) / len(self.grades), 2)
#
#     def __str__(self):
#         return f'{self.name} - {self.average()}'
#
#
# student1 = Student('Vadym Bushmakin')
# student1.add_grade(10)
# student1.add_grade(8)
# student1.add_grade(9)
# student2 = Student('Olha Koval')
# student2.add_grade(5)
# student2.add_grade(12)
# student2.add_grade(7)
# student3 = Student('Ivan Glovo')
# student3.add_grade(8)
# student3.add_grade(3)
# student3.add_grade(10)
# student4 = Student('Illa Lock')
# student4.add_grade(10)
# student4.add_grade(9)
# student4.add_grade(8)
# student5 = Student('Sasha Glock')
# student5.add_grade(8)
# student5.add_grade(9)
# student5.add_grade(7)
#
# st = [student1, student2, student3, student4, student5]
#
# print(student1)
# print(student2)
# print(student3)
# print(student4)
# print(student5)
#
# def enter(students):
#     best = students[0].average()
#     for student in students:
#         if student.average() > best:
#             best = student.average()
#     for stud in students:
#         if stud.average() == best:
#             print(f'Найкращий результат: {stud.name} - {stud.average()}')
#
# enter(st)


#4

# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print(f'Помилка: неможливо додати до балансу {amount}')
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print(f'Помилка: недостатньо коштів для -{amount}')
#
#     def info(self):
#         print(f'{self.owner}: {self.balance}')
#
# walletV = Wallet('Vadym', 1500)
# walletV.deposit(200)
# walletV.deposit(-300)
# walletV.withdraw(500)
# walletV.withdraw(2000)
# walletV.info()
#
# walletV = Wallet('Olha', 3000)
# walletV.deposit(-1000)
# walletV.deposit(500)
# walletV.withdraw(1500)
# walletV.withdraw(20000)
# walletV.info()


#Далі, то я просто у ШІ попросив, щоб він мені дав ще якесь завдання
# і я цого зробив (хотів краще зрозуміти тему). Просто було лінь інший файл робити, тому зробив в цьому.
#не звертайте уваги

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.available = True
#
#     def borrow(self):
#         if self.available:
#             print(f'Тепер ви маєте книгу {self.title}')
#             self.available = False
#         else:
#             print(f'Книги {self.title} наразі немає в наявності')
#
#     def give_back(self):
#         if not self.available:
#             print(f'Ви повернули книгу {self.title} назад')
#             self.available = True
#         else:
#             print(f'Книга {self.title} вже є')
#
#     def __str__(self):
#         if self.available:
#             avail = 'В наявності'
#         else:
#             avail = 'Видана'
#         return f'Книга: {self.title}; Автор: {self.author}; Кількість сторінок: {self.pages}; Статус: {avail}'
#
# book1 = Book('Кобзар', 'Т. Шевченко', '400')
# book1.borrow()
# book1.borrow()
# book1.give_back()
# print(book1)