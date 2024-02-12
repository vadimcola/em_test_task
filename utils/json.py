import json

FILE = './phone_book.json'


def add_data_to_json(data):
    with open(FILE, 'r+') as file:
        json_data = json.load(file)
        json_data.append(data)
        file.seek(0)
        json.dump(json_data, file, indent=4)


def edit_data_in_json(file_name, index, updated_data):
    with open(file_name, 'r+') as file:
        json_data = json.load(file)
        if 0 <= index < len(json_data):
            json_data[index] = updated_data
            file.seek(0)
            json.dump(json_data, file, indent=4)


def delete_data_from_json(file_name, index):
    with open(file_name, 'r+') as file:
        json_data = json.load(file)
        if 0 <= index < len(json_data):
            del json_data[index]
            file.seek(0)
            json.dump(json_data, file, indent=4)


def read_data_from_json():
    with open(FILE, 'r') as file:
        json_data = json.load(file)
        return json_data
