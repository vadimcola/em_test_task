from utils.json import add_data_to_json, read_data_from_json, edit_data_in_json
from utils.utils import add_entry, output_information, search


def main():
    """
    Основная логика приложения Телефонной книги
    """
    while True:
        answer = input(f"Телефонный справочник:\n"
                       f"1: Добавить данные\n"
                       f"2: Вывести список\n"
                       f"3: Поиск по Фамилии\n"
                       f"4: Поиск по Организации\n"
                       f"5: Редактировать контакт по ID\n"
                       f"ВЫХОД: Для выхода из справочника\n"
                       f"   Введите команду...").upper()
        if answer not in ('1', '2', '3', '4', '5', 'ВЫХОД'):
            print("!!!! Ошибка ввода !!!!")
            continue
        elif answer == "ВЫХОД":
            break
        elif answer == '1':
            last_name = str(input('Фамилия:'))
            first_name = str(input('Имя:'))
            middle_name = str(input('Отчество:'))
            organization = str(input('Организация:'))
            work_phone = str(input('Рабочий телефон:'))
            personal_phone = str(input('Персональный телефон:'))
            add_data_to_json(add_entry(last_name, first_name, middle_name,
                                       organization, work_phone, personal_phone))
        elif answer == '2':
            total_pages = (len(read_data_from_json()) + 5 - 1) // 5
            print(f"В справочнике {total_pages} стр.")
            while True:
                page = input(f'Ввидите номер страницы или "+" для возврата в главное меню:')
                if page.isdigit():
                    output_information(read_data_from_json(), int(page))
                elif page == "+":
                    break
                else:
                    print("Вы ввели неверные данные")
        elif answer in ('3', '4'):
            query = input("Введите слово для поиска:").upper()
            search(read_data_from_json(), query)

        elif answer == '5':
            contact_id = int(input("Введите ID контакта..."))
            updated_data = read_data_from_json()
            for i in updated_data:
                if i['id'] == contact_id:
                    print('Введите изменение данных')
                    i['last_name'] = str(input('Фамилия:'))
                    i['first_name'] = str(input('Имя:'))
                    i['middle_name'] = str(input('Отчество:'))
                    i['organization'] = str(input('Организация:'))
                    i['work_phone'] = str(input('Рабочий телефон:'))
                    i['personal_phone'] = str(input('Персональный телефон:'))
                    i['id'] = contact_id
                    edit_data_in_json(updated_data)
                    print("Контакт успешно отредактирован.")


if __name__ == "__main__":
    main()
