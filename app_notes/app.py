import os
import datetime

# считываение файла
def read_file():
    if not os.path.exists("notes.txt"):
        print("\033[31m У вас ещё нет заметок.\033[0m")
        return False
    with open("notes.txt", "r") as file:
        notes = file.read().splitlines()
        if len(notes) == 0:
            print("\033[31m Больше нет заметок.\033[0m")
            return False
        return notes


# создания новой заметки
def create_note():
    title = input("\033[32m Введите заголовок заметки: \033[0m")
    content = input("\033[32m Введите текст заметки: \033[0m")
    mask = "%Y-%m-%d"
    note = f"{title}\n{content}\n{datetime.datetime.now().strftime(mask)}\n"
    
    # Сохраняем заметку в файл
    with open("notes.txt", "a") as file:
        file.write(note)
    
    print("\033[32m Заметка создана успешно.\033[0m")

# чтения списка заметок
def read_notes():
    notes = read_file()
    if not notes:
        return

    print("\033[32m Список заметок: \033[0m")
    for i in range(0, len(notes), 3):
        print(notes[i])
        print("\033[32m " + notes[i + 1] + "\033[0m")
        print("\033[32m " + notes[i + 2] + "\033[0m")

# редактирования заметки
def edit_note():
    title = input("\033[32m Введите заголовок заметки для редактирования: \033[0m")
    
    notes = read_file()
    if not notes:
        return
    
    found = False
    for i in range(0, len(notes), 3):
        if notes[i] == title:
            print("\033[32m Текущий текст заметки: \033[0m")
            print(notes[i + 1])
            new_content = input("\033[32m Введите новый текст заметки: \033[0m")
            notes[i + 1] = new_content
            found = True
            break
    
    if found:
        with open("notes.txt", "w") as file:
            file.write("\n".join(notes) + "\n")
        print("\033[32m Заметка успешно отредактирована.\033[0m")
    else:
        print(f"\033[31m Заметка с заголовком '{title}' не найдена.\033[0m")

# удаления заметки
def delete_note():
    title = input("\033[32m Введите заголовок заметки для удаления: \033[0m")
    
    notes = read_file()
    if not notes:
        return
    
    found = False
    
    for i in range(0, len(notes), 3):
        if notes[i] == title:
            del notes[i:i+3]
            found = True
            break
    
    if found:
        with open("notes.txt", "w") as file:
            file.write("\n".join(notes) + "\n")
        print("\033[32m Заметка успешно удалена.\033[0m")
    else:
        print(f"\033[31m Заметка с заголовком '{title}' не найдена.\033[0m")

# сортировка по дате
def filtered_data_note():
    date = input("\033[32m Введите дату (гггг-мм-дд): \033[0m")

    notes = read_file()
    if not notes:
        return
    
    found = False
    for i in range(0, len(notes), 3):
        if notes[i + 2] == date:
            print(notes[i])
            print("\033[32m " + notes[i + 1] + "\033[0m")
            found = True
    
    if not found:
        print(f"\033[31m Заметок с датой '{date}' нет.\033[0m")

# показать заметку
def open_note():
    title = input("\033[32m Введите заголовок заметки: \033[0m")

    notes = read_file()
    if not notes:
        return
    
    found = False
    for i in range(0, len(notes), 3):
        if notes[i] == title:
            print("\033[32m " + notes[i + 1] + "\033[0m")
            print("\033[32m " + notes[i + 2] + "\033[0m")
            found = True
            break
    if not found:
        print(f"\033[31m Заметка с заголовком '{title}' не найдена.\033[0m")

# Основная функция
def main():
    while True:
        print("\nВыберите команду:")
        print("1. Создать заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выборка по дате")
        print("6. Показать заметку")
        print("7. Выйти")
        
        operation = input("Введите номер команды: ")
        print()
        
        if operation == "1":
            create_note()
        elif operation == "2":
            read_notes()
        elif operation == "3":
            edit_note()
        elif operation == "4":
            delete_note()
        elif operation == "5":
            filtered_data_note()
        elif operation == "6":
            open_note()
        elif operation == "7":
            break
        else:
            print("\033[31m Неверная команда. Попробуйте снова.\033[0m")

main()