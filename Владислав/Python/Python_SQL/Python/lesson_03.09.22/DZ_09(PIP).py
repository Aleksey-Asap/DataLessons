# 1. Даны два списка чисел. 
# Найдите все числа, которые входят как в первый, 
# так и во второй список и выведите их в порядке возрастания.


# from random import randint
 
# a1 = [randint(1, 20) for _ in range(10)]
# a2 = [randint(1, 20) for _ in range(10)]
# print(a1)
# print(a2)
# print(sorted(set(a1).intersection(set(a2))))

# 2. Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES 
# (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось

# a = list(map(int, input().split()))
# newset = set()
# for i in a:
#     print('YES' if i in newset else 'NO')
#     newset.add(i)