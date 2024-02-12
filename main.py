from utils.json import add_data_to_json, read_data_from_json
from utils.utils import add_entry, output_information


def main():
    while True:
        answer = input(f"Телефонный справочник:\n"
                       f"1: Добавить данные\n"
                       f"2: Вывести список\n"
                       f"3: Поиск по Фамилии\n"
                       f"4: Поиск по организации\n"
                       f"4: Редактировать контакт\n"
                       f"   Введите цифру команды...")
        if answer not in ('1', '2', '3', '4'):
            print("!!!! Ошибка ввода !!!!")
            continue
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
                page = int(input("Ввидите номер страницы: "))
                output_information(read_data_from_json(), page)


if __name__ == "__main__":
    main()
