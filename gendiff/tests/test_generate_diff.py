import os
import json
from gendiff.modules.generate import generate_diff


def test_parse_json_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file1_path = os.path.join(current_dir, 'fixtures', 'file1.json')
    file2_path = os.path.join(current_dir, 'fixtures', 'file2.json')

    with open(file1_path) as f1:
        first_file = json.load(f1)
    with open(file2_path) as f2:
        second_file = json.load(f2)

    diff_list = generate_diff(first_file, second_file)
    correct_output = '- follow: false\n'\
                     '  host: hexlet.io\n'\
                     '- proxy: 123.234.53.22\n'\
                     '- timeout: 50\n'\
                     '+ timeout: 20\n'\
                     '+ verbose: true'
    assert correct_output == diff_list
