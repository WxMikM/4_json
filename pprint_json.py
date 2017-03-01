import json
import sys


def load_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file_handler:
            return json.load(file_handler)
    except OSError:
        print('файл "{0}" не может быть открыт'.format(file_path))
    return None


def pretty_print_json(list_json):
    print(json.dumps(list_json, indent=4))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        json_path = input('Введите путь к файлу .json : ')

    list_records = load_data(sys.argv[1] if len(sys.argv) > 1 else json_path)

    if list_records is not None:
        pretty_print_json(list_records)
