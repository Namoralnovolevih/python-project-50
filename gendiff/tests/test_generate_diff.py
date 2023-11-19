import os
from gendiff.modules.generate import generate_diff
from gendiff.parser import parser


def test_json_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file1_path = os.path.join(current_dir, 'fixtures', 'file1.json')
    file2_path = os.path.join(current_dir, 'fixtures', 'file2.json')
    first_file = parser(file1_path)
    second_file = parser(file2_path)
    diff_list = generate_diff(first_file, second_file)
    correct_output = '{\n'\
                     ' - follow: false\n'\
                     '   host: hexlet.io\n'\
                     ' - proxy: 123.234.53.22\n'\
                     ' - timeout: 50\n'\
                     ' + timeout: 20\n'\
                     ' + verbose: true\n'\
                     '}'
    assert correct_output == diff_list


def test_yaml_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file1_path = os.path.join(current_dir, 'fixtures', 'file1.yaml')
    file2_path = os.path.join(current_dir, 'fixtures', 'file2.yaml')
    first_file = parser(file1_path)
    second_file = parser(file2_path)
    diff_list = generate_diff(first_file, second_file)
    correct_output = '{\n'\
                     ' - follow: false\n'\
                     '   host: hexlet.io\n'\
                     ' - proxy: 123.234.53.22\n'\
                     ' - timeout: 50\n'\
                     ' + timeout: 20\n'\
                     ' + verbose: true\n'\
                     '}'
    assert correct_output == diff_list
