# Типы данных:
# int,float,boolean,list,str

# a = 123

# b = 1.23
# type - узнаем тип данных;
# print(type(a))
# print(type(b))


# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, '+', b, '=', a+b)


# f = 1 > 2 or 4 < 6

# print(f)

# a = int(input())
# b = int(input())

# if a > b:
#     print(a)
# else:
#     print(b)

# while

# r = range(10)
# for i in r:
#     print(i)


#  О строках:

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#  print(c)


# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # .

# Cписки

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4


# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# Функции:

# Это фрагмент программы, используемый
# многократно
# def function_name(x):
# body line 1
# . . .
# body line n
# optional return

# def f(x):
#  return x**2

# def f(x):
#  if x == 1:
#  return 'Целое'
#  elif x == 2.3:
#  return 23
#  else:
#  return

# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) #
#
#
#  Практика 1

# 1. Напишите программу, которая принимает на вход
# два числа и проверяет, является ли одно
# число квадратом другого.
# *Примеры:*
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет
#

# number1 = int(input('Введите первое число:'))
# number2 = int(input('Введите первое число:'))
# if number1 **2 ==number2 or number2 ** 2 == number1:
#     print('Да')
# else: print("Нет")
# или
# print('Введите первое число')
# a = int(input())
# print('Введите второе  число')
# b = int(input())
# if a==b*b or b==a*a:
#     print('Да')
# else: print("Нет")

# 2. Напишите программу, которая на вход принимает 5
# чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90
# numbers = []
# for _ in range(5):
#     n = int(input('Введите число: '))
#     numbers.append(n)
# maxx = numbers[0]
# for i in numbers:
#     if i > maxx:
#         maxx = 1
# print(maxx)


# 3.Напишите программу, которая
# будет принимать на вход дробь и
# показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# print('Введите число')
# a = float(input())
# b=a*10%10
# print(int(b))


# 3. Напишите программу, которая принимает на вход
# число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# a = float(input())
# if a % 1 == 0:
#     print('нет')
# else:
#     print(int(a*10)%10)

# print('Введите число')
# a = float(input())
# b=a*10%10
# print(int(b))

#  Напишите программу, которая будет на вход
#  принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
#
# N = int(input())
# for i in range(-N,N):
#     print(i, end=',')
# print(N)

# 3. Напишите программу, которая принимает на вход 
# число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# n = int(input())
# if (n%5 ==0 and  n% 10 == 0 or n % 15 == 0) and n % 30 != 0:
#     print('True')
# else:
#     print('False')