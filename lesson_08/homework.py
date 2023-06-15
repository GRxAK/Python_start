# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

print()
print('------------------------------------------------------------------------------------------------------')
print()

file_path = "file.txt"

def print_header():
    print("..................|..................|..................|...............")
    print(" Фамилия          | Имя              | Отчество         | Номер телефона")
    print("..................|..................|..................|...............")

# показать шапку контактов
def print_contact(line):
    elements = line.split(";")
    for i in range(len(elements) - 1):
        print(" {:<16} |".format(elements[i]), end="")
    print(" " + elements[-1], end="")

# показать все контакты
def show_all_records():
    print_header()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            print_contact(line)
        print()

# поиск контактов
def search_contacts(search):
    with open(file_path, 'r', encoding='utf-8') as f:
        print_header()
        for line in f:
            if search in line:
                print_contact(line)
        print()

# добавление
def add_contact(surname, name, patronymic, nuber):
    with open(file_path, 'a', encoding='utf-8') as f:
        if surname == name == patronymic == '':
            print()
            print("Невозможно добавить контакт, недостаточно информации!")
            return

        f.write("\n")
        f.write(surname.replace(" ",";"))
        f.write(';')
        f.write(name.replace(" ",";"))
        f.write(';')
        f.write(patronymic.replace(" ",";"))
        f.write(';')
        f.write(nuber.replace(" ",";"))


# изменение
def change_contact(contact):
    lines = None
    with open(file_path, 'r', encoding="utf=8") as f:
        lines = f.readlines()

    flag = False
    for i, line in enumerate(lines):
        if contact in line:
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            number = input("Введите номер телефона: ")
            lines[i] = f"{surname};{name};{patronymic};{number}\n"
            flag = True

    if flag:
        with open(file_path, 'w', encoding="utf-8") as f:
            f.writelines(lines)
            print()
            print("Контакт успешно изменен!")
    else:
        print()
        print("Контакт не найдн!")


# удаление
def delet_contact(contact):
    lines = None
    with open(file_path, 'r', encoding="utf=8") as f:
        lines = f.readlines()
    
    flag = False
    for i, line in enumerate(lines):
        if contact in line:
            del lines[i]
            flag = True
    
    if flag:
        with open(file_path, 'w', encoding="utf-8") as f:
            f.writelines(lines)
            print()
            print("Контакт успешно удален!")
    else:
        print()
        print("Контакт не найдн!")




def main():
    select = int(input("Выберите опцию: \n" 
          "    1 - показать телефонный справочник, \n"
          "    2 - найти контакт, \n"
          "    3 - добавить контакт. \n"
          "    4 - изменить контакт, \n"
          "    5 - удалить контакт, \n\n"
          " => "))
    print()

    match select:
        case 1:
            show_all_records()

        case 2:
            data = input("Поиск: ")
            print("")
            search_contacts(data)

        case 3:
            print("Нужно будет ввести данных если каких либо нет, то попустие нажав ENTER")
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            nuber = input("Введите номер телефона: ")
            add_contact(surname, name, patronymic, nuber)

        case 4:
            contact = input("Введите фамилю, имя, отчиство контакта которого хотите ИЗМЕНИТЬ: ")
            change_contact(contact.replace(" ",";"))

        case 5:
            contact = input("Введите фамилю, имя, отчиство контакта которого хотите УДАЛИТЬ: ")
            delet_contact(contact.replace(" ",";"))


main()

print()
print('------------------------------------------------------------------------------------------------------')
print()