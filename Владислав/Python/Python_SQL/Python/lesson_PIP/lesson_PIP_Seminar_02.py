# тип данных (пустое множество)
# set()

# a = set() # пустое множество
# и = {1,3,4,9,10}
# Из списка можно сделать множество
# c = [1,2,3,3,3,4,5]
# c = set(c) # Оставил уникальныные в списки
# print(c)
# c.add(10)
# print(c)
# Удалить число -discard()
# c.discard(5)
# print(c)

# Представлен список чисел. Определить элементы списка, 
# не имеющие повторений.
# Сформировать из этих элементов список с 
# сохранением порядка их следования в исходном
# списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение 
# «в лоб». Потом подумайте об оптимизации.


# from collections import Counter   # Находит сам элемент потом кол-во, сколько он встречается в списке
# scr = [2,2,2,7,23,1,44,44,3,2,10,7,4,11]

# # ls = [i for i in scr if scr.count(i) == 1]

# # print(ls)
# str_1 = list(set(scr))
# ls_2 = [i for i in str_1 if scr.count(i) == 1]
# print(ls_2)

# ls_3 =Counter(scr)
# print(ls_3)

# s = input()
# set_s = list(set(s))
# s_final = ''
# s_final = ''.join(set_s)
# print(set_s)
# print(s_final)
# print(''.join(list(set(input()))))

print(*sorted(set(input().split()) & set(input().split()), key=int))