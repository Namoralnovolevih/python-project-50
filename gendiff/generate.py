from gendiff.format.stylish import make_stylish
from gendiff.format.plain import make_plain
from gendiff.format.json import format_json
from gendiff.parser import parser
import os


TYPE = 'status'
VALUE = 'value'


FORMAT_FUNCTIONS = {'stylish': make_stylish,
                    'plain': make_plain,
                    'json': format_json,
                    }


DEFAULT_FORMAT_FUNCTIONS = 'stylish'


def read_data(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_diff(old_data: dict, new_data: dict) -> dict:
    old_keys = list(old_data.keys())
    new_keys = list(new_data.keys())
    keys = set(old_keys + new_keys)

    res = {}

    for key in sorted(keys):
        old_value = old_data.get(key)
        new_value = new_data.get(key)

        if isinstance(old_value, dict) and isinstance(new_value, dict):
            res[key] = {TYPE: 'nested',
                        VALUE: get_diff(old_value, new_value)
                        }

        elif key in old_keys and key not in new_keys:
            res[key] = {TYPE: 'removed',
                        VALUE: old_value}

        elif key not in old_keys and key in new_keys:
            res[key] = {TYPE: 'add',
                        VALUE: new_value}

        elif old_value == new_value:
            res[key] = {TYPE: 'unchanged', VALUE: old_value}

        else:
            res[key] = {TYPE: 'changed',
                        'old_value': old_value,
                        'new_value': new_value}

    return res


def generate_diff(path_file1: str,
                  path_file2: str,
                  format=DEFAULT_FORMAT_FUNCTIONS
                  ) -> str:
    file1 = read_data(path_file1)
    file2 = read_data(path_file2)
    _, format_file1 = os.path.splitext(path_file1)
    _, format_file2 = os.path.splitext(path_file2)
    old_data = parser(file1, format_file1.strip("."))
    new_data = parser(file2, format_file2.strip("."))

    if old_data == new_data:
        return ''

    values = get_diff(old_data, new_data)

    res = FORMAT_FUNCTIONS[format](values)

    return res
