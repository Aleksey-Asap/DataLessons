# my_list = [1,1,2,3,4,4,5]
# print(tuple(filter(lambda num: my_list.count(num)==1,my_list)))

# Лекция

x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b

def sum():
    return x + y
