# 1. Напишите программу, которая принимает 
# на вход вещественное число и показывает 
# сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input('Введите число: ')
# summ = 0
# for i in number:
#     if i.isdigit():
#         summ += int(i)
# print(summ)

# 2. Напишите программу, которая принимает 
# на вход число N и выдает набор произведений 
# чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input())
# fact = 1
# some_list = []
# for i in range(1, N + 1):
#     some_list.append(fact * i)
#     fact *= i
# print(some_list)

# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:

# n = int(input())
# summ = 0
# for i in range(1, n + 1):
#     summ += (1 + 1/i) ** i
# print(summ)

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания спис

# from random import *
# n = int(input())

# some_list = [randint(-n,n) for _ in range(randint(5,10))]
# print(some_list)

# f = open('17.txt', 'w')
# for i in range(randint(2, len(some_list))):
#     f.write(str(randint(0, len(some_list)-1)) + '\n')
# f.close

# pr = 1
# with open('17.txt', 'r') as f:
#     for i in f.read().splitlines():
#         pr = pr*some_list[int(i)]
# print(pr)