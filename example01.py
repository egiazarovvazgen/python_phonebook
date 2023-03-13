def open_file():
    with open(path, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(";"):
                cont.append(field.strip())
            phonebook.append(cont)


def save_file():
    with open(path, "w", encoding="UTF-8") as file:
        i = 0
        while i < len(phonebook):
            phonebook[i] = ";".join(map(str, phonebook[i]))
            i += 1
        new_phonebook = "\n".join(map(str, phonebook))
        file.write(new_phonebook)


def show_all_contacts():
    for i, contact in enumerate(phonebook, 1):
        print(f"{i}. {contact[0]:<25}{contact[1]:<25}{contact[2]:<25}")


def create_contact():
    full_name = input("Введите имя и фамилию: ")
    phone_number = input("Введите телефонный номер: ")
    comment = input("Введите комментарий: ")
    phonebook.append(list([full_name, phone_number, comment]))


def change_contact():
    key_element = input("Введите ключевой элемент контакта: ")
    for i, contact in enumerate(phonebook, 1):
        for field in contact:
            if key_element in field:
                print(f"{i}. {contact[0]:<25}{contact[1]:<25}{contact[2]:<25}")
                variable_value = int(input("Введите '1', если хотите изменить имя и фамилию, "
                                           "'2', если хотите изменить телефонный номер, "
                                           "'3', если хотите изменить комментарий: "))
                match variable_value:
                    case 1:
                        new_full_name = input("Введите новое имя и новую фамилию: ")
                        contact[0] = new_full_name
                    case 2:
                        new_phone_number = input("Введите новый телефонный номер: ")
                        contact[1] = new_phone_number
                    case 3:
                        new_comment = input("Введите новый комментарий: ")
                        contact[2] = new_comment


def find_contact():
    key_element = input("Введите ключевой элемент контакта: ")
    for i, contact in enumerate(phonebook, 1):
        for field in contact:
            if key_element in field:
                print(f"{i}. {contact[0]:<25}{contact[1]:<25}{contact[2]:<25}")


def delete_contact():
    key_element = input("Введите ключевой элемент контакта: ")
    for i, contact in enumerate(phonebook, 1):
        for field in contact:
            if key_element in field:
                removal_control = int(input(f"Вы действительно хотите удалить этот контакт: "
                                            f"{i}. {contact[0]:<25}{contact[1]:<25}{contact[2]:<25}?"
                                            f"\nВведите '1', если 'да', '2', если 'нет': "))
                match removal_control:
                    case 1:
                        phonebook.remove(contact)
                        print("Контакт удалён успешно")
                    case 2:
                        print("Выберите другой пункт главного меню")


phonebook = []
path = "contacts.txt"
while True:
    print("""Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Изменить контакт
    6. Найти контакт
    7. Удалить контакт
    8. Выход""")
    a = int(input("Выберите пункт: "))
    match a:
        case 1:
            open_file()
            print("Файл открыт успешно")
        case 2:
            save_file()
            print("Файл сохранён успешно")
        case 3:
            show_all_contacts()
        case 4:
            create_contact()
            print("Контакт создан успешно")
        case 5:
            change_contact()
            print("Контакт изменён успешно")
        case 6:
            find_contact()
        case 7:
            delete_contact()
        case 8:
            break
print("До свидания!")
