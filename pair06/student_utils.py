from random import *
from statistics import mean

def generate_grades(count):
    grades = []
    for i in range(count):
        grades.append(randint(1, 12))
    return grades

def average_grade(grades):
    return round(mean(grades), 2)

def get_level(average):
    if average < 4:
        return 'Початковий рівень'
    elif 4 <= average <= 6.99:
        return 'Середній рівень'
    elif 6.99 < average <= 9.99:
        return 'Достатній рівень'
    else:
        return 'Високий рівень'
