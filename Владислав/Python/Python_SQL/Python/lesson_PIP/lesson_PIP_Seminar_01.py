# name - ключ, Ivan - значение ключа. Словарь
# from distutils.command.build_scripts import first_line_re


# some_dict = {'name': 'Ivan',
#              'last_name': 'Ivanov',
#              'age': 32
#             }
# print(some_dict['age'])
# get- Получаем искомное значение из списка. Вместо None в комндной строке будет "Ключ не найден"
# print(some_dict.get('sdkl', 'Ключ не найден'))

# Метод setdefault. В словарь добавляем еще 1 элемент
# print(some_dict.setdefault('adress','Berezovaya 1'))
# print(some_dict)

# Есть два списка они вводяться пользователями.
# Нам нужно ввести элементы, сгенерировать эти элементы.
# Получить словарик,значение первых элементов равно значению вторых элементов из списка.

# first_list = [1,2,3,4,5]
# second_list = ['a','b','c','d','e']
# some_dict = {}
# for i in range(len(first_list)):
#     some_dict[first_list[i]] = second_list[i]
# print(some_dict)


# 1. Написать функцию num_translate(), переводящую числительные
# от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one") "один"
# >>> num_translate("eight")"восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где
# лучше хранить информацию, необходимую для перевода: какой тип данных выбрать,
# в теле функции или снаружи.

# from fnmatch import translate


# first_list = ['zero','one','two','three']
# second_list = ['ноль','один','два','три']
# some_dict = {}
# for i in range(len(first_list)):
#     some_dict[first_list[i]] = second_list[i]
# print(some_dict)

# print(some_dict.get(input('Введите англиское число:'), 'Нет значения'))


# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One") "Один"
# >>> num_translate_adv("two") "два"

# def num_translate(number):
#     translate_dict = {'one': 'один','two': 'два', 'three': 'три'}
#     if number[0].isupper():
#         print(translate_dict.get(number.lower()).capitalize())
#     else:
#         print(translate_dict.get(number))
# num_translate('One')
# num_translate('one')
# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена
# сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
# "И": ["Иван", "Илья"],
# "М": ["Мария"], "П": ["Петр"]
# }

# from hashlib import new


# some_list = ["Иван","Мария","Петр","Илья"]
# some_dict ={}

# new_list = []
# for i in range(len(some_list)):
#     if some_list[i][0] in some_dict:
#         some_dict[some_list[i][0]].append(some_list[i])
#     else:
#         some_dict[some_list[i][0]] = [some_list[i]]
# print(some_dict)

def thesaurus(*args):
    some_dict = {}

    for i in args:
        if i[0] in some_dict.keys():
            some_dict[i[0]].append(i)
        else:
            some_dict[i[0]] = [i]
    print(some_dict)

thesaurus("Иван", "Мария", "Петр", "Илья")

#  4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
