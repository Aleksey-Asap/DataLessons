def get_process():
    return int(input('Экспорт - это 1, импорт - это 2, сделайте выбор: '))

def get_structure():
    return int(input('Выберите формат: по-строчно - 1; через "," - 2 '))

def get_first_surname():
    return input('Фамилия:')

def get_last_name():
    return input('Имя:')    

def get_tel():
    return input('Телефон:') 

def get_description():
    return input('Описание:') 

def view(data):
    print(data)