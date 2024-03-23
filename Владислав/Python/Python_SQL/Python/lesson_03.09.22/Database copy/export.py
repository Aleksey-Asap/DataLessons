def expp(last_name):
    with open('Python\lesson_03.09.22\Database copy\Data.txt', 'r', encoding='utf-8') as b:
        info_list = b.read().splitlines()
        for person in info_list:
            if last_name in person:
                print(person)
