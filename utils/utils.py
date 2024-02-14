def add_entry(last_name, first_name, middle_name,
              organization, work_phone, personal_phone):
    """
    Функция создает словарь с данными телефонной книги
    """
    entry = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'organization': organization,
        'work_phone': work_phone,
        'personal_phone': personal_phone
    }
    return entry


def search(data, query):
    """
    Функция поиска и вывода информации из телефонной книги
    """
    results = []
    for entry in data:
        if entry['last_name'].upper() == query or entry['organization'].upper() == query:
            results.append(entry)

    for item in results:
        print(f"{'*' * 200}\n"
              f"ID записи {item['id']}\n"
              f"{item['last_name'].upper()} {item['first_name'].upper()} {item['middle_name'].upper()}\n"
              f"Организация:{item['organization'].upper()}\n"
              f"Телефон рабочий:{item['work_phone'].upper()}\n"
              f"Телефон личный: {item['personal_phone'].upper()}")

    if len(results) == 0:
        print("Контактов с таким запрсом нет !!!")


def output_information(data, page):
    """
    Функция вывода постраичной информации телефонной книги
    на каждой страницы выводится по 5 записей.
    """
    items_per_page = 5
    total_pages = (len(data) + items_per_page - 1) // items_per_page

    if page < 1 or page > total_pages:
        print("Неверный номер страницы. Пожалуйста, введите действительный номер страницы.")
        return

    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    page_data = data[start_index:end_index]

    for item in page_data:
        print(f"{'*' * 200}\n"
              f"ID записи {item['id']}\n"
              f"{item['last_name'].upper()} {item['first_name'].upper()} {item['middle_name'].upper()}\n"
              f"Организация:{item['organization'].upper()}\n"
              f"Телефон рабочий:{item['work_phone'].upper()}\n"
              f"Телефон личный: {item['personal_phone'].upper()}")

    print(f"{'*' * 200}\n"
          f"Страница №{page}")

    if page > 1:
        print("Предыдущая страница:", page - 1)

    if page < total_pages:
        print("Следующая страница:", page + 1)
