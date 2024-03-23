# 1. Задайте строку из набора чисел. Напишите программу, 
# которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.


# Сокращено:
# ls = list(map(int, input().split())) # map - это функция, в данном случае, которая привращает текст в число. 

# tekst = '1 2 3 4 5'.split()
# print(tekst) 
# def s(n):
#     return n*2
# tekst = map(int, tekst)
# print(tekst) # строки превращаюстя в числа
# tekst = list(tekst)
# print(tekst)
# tekst = map(s, tekst) # применяем нашу функцию s , ко всем обхектам в новом списке
# print(list(tekst))

# some_str = input() # '1 2 3 4 5'
# some_list = some_str.split() # ['1', '2', '3', '4', '5']
# some_int_list = list(map(int, some_list))# [1,2,3,4,5]
# print(some_int_list)
# print(max(some_int_list), min(some_int_list))


# 2. Найдите корни квадратного уравнения 
# Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения 
# корней квадратного уравнения

# a = int(input())
# b = int(input())
# c = int(input())
# d = b**2 - 4*a*c
# if d < 0:
#     print('Корней нет')
# elif d == 0:
#     print(-b / 2*a)
# else:
#     print((-b+d**(1/2))/2*a)
#     print((-b-d**(1/2))/2*a)

# 2) с помощью дополнительных библиотек Python
# import sympy as sm
# x = sm.Symbol('x')
# a = int(input())
# b = int(input())
# c = int(input()) 
# print(sm.solveset(a*x**2 + b*x*c, x))

# 3. Задайте два числа. Напишите программу, которая 
# найдёт НОК (наименьшее общее кратное) этих двух чисел.

