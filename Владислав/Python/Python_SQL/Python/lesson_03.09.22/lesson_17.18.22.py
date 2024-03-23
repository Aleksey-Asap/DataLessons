# 1. В файле находится N натуральных чисел, записанных через пробелю
# Среди чисел не хватает одного, чтобы выполнить условие A[i] - 1 =A[i-1].
# Найдите это число

# 1 способ:
# num = ''

# def fun(num):
#     for i in range(0, len(num)):
#         if (num[i+1]) -num[i] != 1:
#             return num[i]+1

# with open('numfile.txt', 'r') as data:
#     num = data.read()
# num = list(map(int,num.split(', ')))

# print(fun(num))


# 2 способ:


# 2. Дан список чисел. Создайте список, в который попадают числа,
# описывающие возврастающую последовательность. Порядок элементов менять нельзя.

# num = [1, 5, 2, 3, 4, 6, 1, 7]

# def nextmax(listt):
#     max = listt[0]
#     res = [listt[0]]
#     for i in range(len(listt)):
#         if listt[i] > max:
#             max = listt[i]
#             res.append(max)
#     return res

# print(nextmax(num))
# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# res = [my_list[0]]
# [res.append(item) for item in my_list if item > res[-1]]
# print(res)


# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв"
# "Мы неабв очень любим Питон иабв Джавуабв!"

# print(' '.join(filter(lambda X: not 'абв' in X,'Мы неабв очень любим Питон иабв Джавуабв'.split())))
