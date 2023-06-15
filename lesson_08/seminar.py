# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


file_path = "file.txt"


def show_all_records():
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(*line.strip().split(';'))


def search_record(search):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if search in line:
                # print(line, end='')
                print(*line.strip().split(';'))


def add_contact(fio, number):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write("\n")
        f.write(fio.replace(" ",";"))
        f.write(';')
        f.write(number)


def main():
    select = int(input("Выберите опцию:" 
          " 1 - показать телефонный справочник,"
          " 2 - найти контакт,"
          " 3 - добавить контакт. => "))

    match select:
        case 1:
            show_all_records()
        case 2:
            data = input("Поиск: ")
            search_record(data)
        case 3:
            fio = input("Введите имя: ")
            number = input("Введите номер телефона: ")
            add_contact(fio, number)

main()