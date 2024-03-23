# 1. Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора 
# псевдослучайных чисел.

# import time

# n = time.time_ns()

# print(time.time_ns())
# print(str(n)[-3])

# 2. Задайте список. Напишите программу, 
# которая определит, присутствует ли в заданном 
# списке строк некое число.
# sp = []
# for _ in range(7):
#     sp.append(input()) # append - добавляет в конец списка значение и input туда забрасывает строку 

# print(sp)

# n = int(input())

# flag = False
# for i in sp:
#     if str(n) in i:
#         flag = True
#         print('Число есть в элементе списка')
#         break
# if not flag:
#         print('Числа в списке не оказалось')

some_list = [input('Введите строку: ') for _ in range(int(input('Введите кол-во элементов: ')))]
el = input('Введите искомое число: ')
for i in some_list:
    if el in i:
        print('Yes')
        break
else:
    print('No')



# 3. Напишите программу, которая определит 
# позицию второго вхождения строки в 
# списке либо сообщит, что её нет.


# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1'

# some_list = [input('Введите строку: ') for _ in range(int(input('Введите кол-во элементов: ')))]
# el = input('Введите искомую строку: ')
# c = 0
# if some_list.count(el) != 2:
# print(-1)
# else:
# for i in range(len(some_list)):
# if some_list[i] == el:
# c += 1
# if c == 2:
# print(i)
# break

# some_list = [input('Введите строку: ') for _ in range(int(input('Введите кол-во элементов: ')))]
# el = input('Введите искомую строку: ')
# try:
# print(some_list.index(el, some_list.index(el) + 1))
# except:
# print(-1)