def add_entry(last_name, first_name, middle_name,
              organization, work_phone, personal_phone):
    entry = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'organization': organization,
        'work_phone': work_phone,
        'personal_phone': personal_phone
    }
    return entry


def edit_entry():
    pass


def search(data, query):
    results = []
    for entry in data:
        if entry['last_name'] == query or entry['organization'] == query:
            results.append(entry)
    return results


def output_information(data, page):
    items_per_page = 5
    total_pages = (len(data) + items_per_page - 1) // items_per_page

    if page < 1 or page > total_pages:
        print("Неверный номер страницы. Пожалуйста, введите действительный номер страницы.")
        return

    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    page_data = data[start_index:end_index]

    for item in page_data:
        print(item)

    print(f"Страница {page}/{total_pages}")

    if page > 1:
        print("Предыдущая страница: ", page - 1)

    if page < total_pages:
        print("Следующая страница: ", page + 1)
