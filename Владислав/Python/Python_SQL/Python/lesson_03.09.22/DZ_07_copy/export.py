from user_interface import get_first_surname
from user_interface import get_last_name
from user_interface import get_tel
from user_interface import get_description
def export_structure():
    first_name = get_first_surname()
    last_name = get_last_name()
    tel = get_tel()
    description = get_description()
    with open('Python\lesson_03.09.22\DZ_07_copy\data_phone1.txt', 'a') as file:
        file.write('{}\n{}\n{}\n{}\n\n'\
            .format(first_name, last_name, tel, description))
