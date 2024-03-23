# def view_data(data):
#     print(f'sum = {data}')

# def get_value():
#     return int(input('value = '))


a = list(map(int, input().split()))
newset = set()
for i in a:
    print('YES' if i in newset else 'NO')
    newset.add(i)