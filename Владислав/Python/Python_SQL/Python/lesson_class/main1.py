# class Auto:
#     # Инициализация. Метод вызывается при создании объекта 
#     def __init__(self):
#         print("Автомобиль заведен")
#        # Атрибуты объекта (auto_name - публичный доступ)
#         self.auto_name = 'lexus'
#         # _ - нет защищенности
#         self._auto_year = 2019
#         # __ - Приватное (защищенный доступ)
#         self.__auto_model = 'RX 350L'
# # Создаем ообъект класса auto:

# a=Auto()
# print(a.auto_name)
# print(a._auto_year)
# print(a._Auto__auto_model)

# Класс Transport
# class Transport: 
#     def transport_method(self):
#         print("Это родительский метод из класса Transport")

# # Класс Auto, наследующий Transport 
# class Auto(Transport):
#     def auto_method(self):
#         print("Это метод из дочернего класса")