import json

FILE = './phone_book.json'


def add_data_to_json(data):
    """
    функция добовляет данные в JSON файл
    """
    with open(FILE, 'r+') as file:
        json_data = json.load(file)
        if not json_data:
            data['id'] = 1
        else:
            last_id = json_data[-1]['id']
            data['id'] = last_id + 1
        json_data.append(data)
        file.seek(0)
        json.dump(json_data, file, indent=4)


def edit_data_in_json(updated_data):
    """
    Функция для добовления отредактированных данных в JSON файл
    """
    with open(FILE, "w") as file:
        json.dump(updated_data, file)


def read_data_from_json():
    """
    Функция чтения JSON файла
    """
    with open(FILE, 'r') as file:
        json_data = json.load(file)
        return json_data
