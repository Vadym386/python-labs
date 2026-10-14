# import math
# from math import *
# import statistics as stat
# import random
# from datetime import date
# import demo
# from tkinter import *

# print(math.sqrt(81))

# a = [10, 15, 8, 9, 3]
# print(f"Середній бал: {stat.mean(a)}")
# r = int(input('r = '))
# circle_area = round(pi * pow(r, 2), 2)
# print(circle_area)

# balls = 25
# n = 6
# print(f'Повністю заповнених коробок: {flor(balls / n)}')
# print(f'Всього коробок: {ceil(balls / n)}')

# numbers = []
# for i in range(10)
#     numbers.append(random.randint(1,100))
#     print(f'Випадкові 10 чисел: {numbers}')
#
# selected = random.choice(numbers)
# print(f'Випадкове із послідовності: {selected}')
#
# print(f'Сьогодні: {date.today()}')
#
# print(demo.squre(5))
# print(demo.is_even(7))
# grades = [12, 5, 7, 9]
# print(demo.average(grades))


# def text():
#     lbl_text['text'] = 'hello world'
#
# def clear():
#     lbl_text['text'] = ''
#
# window = Tk()
# window.title('my first window')
# window.geometry('500x400')
# window.resizable(False, False) #забороняє змінювати розмір
# window['bg'] = '#F19CBB'
#
# label = Label(window, text = 'Супер-пупер програма', font = ('Arial', 18), bg = '#F19CBB', pady = 20)
# label.pack()
# # label.place(x = 0, y = 0)
# frame = Frame(window, bg = '#F19CBB')
# frame.pack()
# bt1 = Button(frame, text = 'OK', width = 7, activebackground = 'lightgreen', command = text)
# bt1.grid(row = 0, column = 0) #ряд і колонка
# bt2 = Button(frame, text = 'Cancel', width = 7, activebackground = 'lightgreen', command = clear)
# bt2.grid(row = 0, column = 1, padx = 10) #кнопки роз'їхались по х
#
# lbl_text = Label(frame, text = '', font = ('Arial', 18), bg = '#F19CBB', pady = 20)
# lbl_text.grid(row = 1, column = 0, columnspan = 2)
#
#
# window.mainloop() #запускає вікно