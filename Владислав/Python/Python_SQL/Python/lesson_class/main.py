# class Auto:
#     #атрибуты класса
#     auto_name = 'lexus'
#     auto_model = 'RX 350L'
#     auto_year = 2019

#     #Методы класса
#     def on_avto_start(self,auto_name,auto_model,auto_year):
#         print(f'Заводим автомобиль')

#     def on_auto_stop(self):
#         print('Останавливаем работу двигателя')

# a = Auto()
# print(a)
# print(type(a))
# print(a.auto_name)
# a.on_avto_start()
# a.on_auto_stop()


# class Auto:
#     #атрибуты класса
#     auto_count=0

#     #Методы класса
#     def on_avto_start(self,auto_name,auto_model,auto_year):
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         print(f'Заводим автомобиль')
#         Auto.auto_count += 1

# a = Auto()
# a.on_avto_start('lexus','RX 350L',2019)
# print(a.auto_name)
# print(a.auto_count)

# a_2 = Auto()
# a_2.on_avto_start('Audy','350L',2019)
# print(a_2.auto_name)


# Конструктор:

# class Auto:
#     auto_count = 0

#     def __init__(self, auto_name, auto_model):
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         Auto.auto_count += 1
#         print(Auto.auto_count)
# a_1 = Auto('Audi', 'A4')
# a_2 = Auto('BMW','M5')


#Задание 1 напишите класс
# class LittleBell:
#     def sound(self):
#         print('fdsf')

# bell = LittleBell()
# bell.sound()
# bell.sound()
# bell.sound()

# class Button:
#     count = 0

#     def click(self):
#         Button.count += 1

#     def click_count(self):
#         return Button.count

#     def reset(self):
#         Button.count = 0


# button = Button()
# button.click()
# button.click()
# print(button.click_count())
# button.reset()
# print(button.click_count())

#Задание 2 напишите класс

# class Big_bell:
#     def __init__(self):
#         self.count = 1

#     def sound(self):
#         self.count += 1
#         if not self.count % 2:
#             print('ding')
#         else:
#             print('dong')

# bell = Big_bell()
# bell.sound()
# bell.sound()
# bell.sound()

# bell_2 = Big_bell()
# bell_2.sound()

#Задание 3 напишите класс

# Формат ввода
# Каждый тест представляет собой код, в котором будет использоваться ваш класс.
# Файл с решением не обязательно называть solution.ру, он будет переименован 
# автоматически. Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.
#Пример:
# Ввод
# from solution import Balance

# balance = Balance()
# balance.add_right(10)
# balance.add_left(9)
# balance.add_left(2)
# print(balance.result())

# Вывод : L

# class Balance:
#     def __init__(self):
#         self.left = 0
#         self.right = 0

#     def add_left(self, weight):
#         self.left += weight

#     def add_right(self, weight):
#         self.right += weight

#     def result(self):
#         if self.left < self.right:
#             return 'R'
#         elif self.left > self.right:
#             return 'L'
#         else:
#             return '='

# ballance = Balance()
# ballance.add_right(10)
# ballance.add_left(9)
# ballance.add_left(2)
# print(ballance.result())

# Задание 4 напишите класс


# class OddEvenSeparator():

#     def __init__(self):
#         self.odd = []
#         self.even = []

#     def add_number(self, num):
#         if not num % 2:
#             self.even.append(num)
#         else:
#             self.odd.append(num)

# separator = OddEvenSeparator()
# separator.add_number(1)
# separator.add_number(5)
# separator.add_number(6)
# separator.add_number(8)
# separator.add_number(3)
# print(separator.even)
# print(separator.odd)
