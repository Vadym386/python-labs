# book_dict = {
#     'title': 'Кобзар',
#     'author': 'Тарас Шевченко',
#     'copies': 15
# }
# print(book_dict['title'])


# class Book:
#     def __init__(self, title, price, copies):
#         self.title = title
#         self.price = price
#         self.copies = copies
#
#     def avaliable(self):
#         return self.copies > 0
#
# book1 = Book('Кобзар', 450, 15)
# book2 = Book('Лісова пісня', 500, 0)
# print(book1.title, book1.price)
# print(book1.price)
# print(book2.title, book2.price)
# для запуску класу використовується __init__
# self - конкретний об'єкт

# print(f'Кобзар доступний: {book1.avaliable()}')
# print(f'Лісова пісня доступний: {book2.avaliable()}')


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#     def area(self):
#         return self.width * self.height
#     def info(self):
#         print(f'Розміри прямокутника {self.width}x{self.height}')
#         print(f'S = {self.area()}')
#         print(f'P = {self.perimeter()}')
#
# a = int(input('Введіть ширину: '))
# b = int(input('Введіть довжину: '))
# rectangle = Rectangle(a, b)
# rectangle.info()