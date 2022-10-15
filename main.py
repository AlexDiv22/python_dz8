from import_data import *
from export_data import export_data
from print_data import print_data
from search_data import search_data
from input_data import input_data

def choice_todo():
    print("Введите цифру необходимого действия:\n\
    1 - Добавить студента;\n\
    2 - Вывести на экран всех студентов;\n\
    3 - Поиск студента;\n\
    Выход - нажмите любой символ")
    print()
    ch = input("Жду ввода ")
    print()
    if ch == '1':
        import_data(input_data())
        print()
        return choice_todo()
    elif ch == '2':
        data = export_data()
        print_data(data)
        print()
        return choice_todo()
    elif ch == '3':
        word = input("Введите данные для поиска: ")
        print()
        data = export_data()
        item = search_data(word, data)
        if item not in data:
           print("Данные не обнаружены")
           print()
        else:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
            print("_"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
            print()
        return choice_todo()
    else:
        exit()