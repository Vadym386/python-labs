from student_utils import *
from tkinter import *

students = input('Учні: ').strip().split(', ')
grades = int(input('Кількість оцінок: '))
all_result = ''
for st in students:
    gen = generate_grades(grades)
    av = average_grade(gen)
    result = f'{st}: {gen} → {av} → {get_level(av)}'
    print(result)
    all_result += result + '\n'

def show():
    label['text'] = all_result

window = Tk()
window.title('Статистика')
window.geometry('600x400')
window.resizable(False, False)
window['bg'] = 'lightblue'

label = Label(window, text = '', font = ('Arial', 16), bg = 'lightblue', fg = 'darkred', pady = 16)
label.pack()
bt = Button(window, text = 'Show', font = ('Arial', 16), command = show)
bt.pack()
window.mainloop()