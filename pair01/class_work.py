#a = 12 #int
#b = 12.43 #float
#c = '12' #srt
#d = True #bool False

# + -
# * / // %
# b ** a степінь

#print('Ok')
#n = int(input('введи число: ')) #Якщо дужки - це функція
#m = int(input('введи число: '))
#print(n + m) #Конкатенація - додавання двох або більше стрінгових частин

#int()
#float()
#str()
#bool()
#type()

#a = int(input())
#b = int(input())

# a, b = map(int, input().split())
# print(a + b)

a = int(input())
b = int(input())
c = int(input())
# < > <= >= !=
# or and not
if a > b and a > c:
    print(a)
elif a < b and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print('a == b == c')