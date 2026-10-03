# name = 'Vadym'
# age = '18'
# print(len(name)) #визначає кількість символів
# print(name[0])
# print(name[10])
# print((name[len(name)-1]))

# text = input()
# if len(text) > 0:
#     print(text[0])
# else:
#     print('Imposible')

# text = 'heLlo woRld'
# print(text[:5])
# print(text[6:])
# print(text[::2])
# print(text[::-1])

# стрінговий тип - незмінна колекція

# text[1] = '3' не можна

# print(text.upper()) кепс
# print(text)
# print(text.lower()) маленькі літери
# print(text.title()) перші з великої
# print(text.capitalize()) тільки перша у тексті велика

# text = '    python  '
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())

# user_login = 'admin'
#
# login = input("Enter your login : ").strip().lower()
# if user_login == login:
#     print("Welcome " + user_login)


# text = 'python'
# for i in text:
#     print(i)

# password = input() #дві цифри цифра, два символи кепсом, довжина > 8
# digits = 0
# u_letter = 0
# if len(password) >= 8:
#     for char in password:
#         if char.isdigit():
#             digits += 1
#         if char.isupper():
#             u_letter += 1
#     if digits >= 2 and u_letter >=2:
#         print('Ok')
#     else:
#         print('Wrong')

# password.isdigit() цифри
# password.isupper() великі літери
# password.islower() маленькі літери
# password.isalpha() літери
# password.isalnum() тільки літери і цифри, без знаків

# golosni = 'аеєиїоуяію'
# count = 0
# text = input('веди текст: ').lower()
# for char in text:
#     if char in golosni:
#         count += 1
# print(count)

# text = ('Hello World! Python is the best')
# words = text.split()
# print(words)
#
# result = '-'.join(words)
# print(result)
#
# new_text = text.replace('Python', 'JavaScript')
# print(new_text)

# text = input().lower().strip()
# if text == text[::-1]:
#     print('Palindrom')
# else:
#     print('Not Palindrom')

# text = input().strip().lower()
#
# words = text.split()
# max_word = words[0]
# for word in words:
#     if len(word) > len(max_word):
#         max_word = word
# print(max_word)