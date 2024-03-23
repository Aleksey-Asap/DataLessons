# 30. Вычислить число pi c заданной точностью d
# Пример: при d = 0.001,  pi = 3.141. 10^(-1) <= d10 <= 10^(-10)

# from math import pi
# d = int(input("Введите точность (до 15ти знаков после запятой включительно), c которой хотите получить число Пи:\n"))
# my_str = str(pi)
# my_lst = []
# for i in range(d + 2):
#     my_lst.append(my_str[i])
# my_pi = "".join(my_lst) # join - соединяет список (буквы), остается в формате текса, с числами он не работает.
# print(f"число Пи с заданной точностью {d} равно {my_pi}")

# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# 16 = 2 * 2 * 2 * 2 * 1
# 21 = 3 * 7 * 1
# 24 = 2 * 2 * 2 * 3 

# N = int(input('Введите натуральное число:'))
# lst_dev = [1]
# while N != 1:
#     for i in range(2, N + 1):
#         if N % i == 0:
#             lst_dev.append(i)
#             N = N // i
#             break
# print(lst_dev)
# unique_dev = list(set(lst_dev))
# print(f'Уникальные значения: {unique_dev}')

# 32. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

# number = [1,2,3,4,5,5,2]
# number = list(set(number)) # set - множество хранит в себе только уникальные значения
# print(number)


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint 
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     return [randint(1, 10) for i in range (k + 1)] # если К=3 то в переменной сгенерируеться список со случайными числами от 1 до 10


# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     # как встроенная функция zip, но берет самый длинный итератор, а более короткие дополняет fillvalue.
#     # генерирует члены уравнения
#     polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue='') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     # возвращает по одному элементу из первого итератора, потом из второго, до тех пор, пока итераторы не кончатся
#     # раскрываем списки внутри списка
#     polynomial = list(itertools.chain(*polynomial))

#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x', ' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('1.txt', 'w') as data:
#     data.write(polynom1)


# # Второй многочлен для следующей задачи:

# k = randint(2, 5)

# ratios = get_ratios(k)
# polynom2 = get_polynomial(k, ratios)
# print(polynom2)

# with open('2.txt', 'w') as data:
#     data.write(polynom2)

# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


