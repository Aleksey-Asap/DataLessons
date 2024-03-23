import Import
import Input
import export

user = Input.user_choice()
if user == '1':
    str1, str2, str3, str4, str5 = Input.Data()
    print(str1, str2, str3, str4, str5)
    str0 = ' '
    Import.add(str1)
    Import.add(str2)
    Import.add(str3)
    Import.add(str4)
    Import.add(str5)
    Import.add('')
elif user == '2':
    export.print_baza()
else:
    print('Введена недопустимая информация!') 


