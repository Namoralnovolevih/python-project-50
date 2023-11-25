import pytest
from gendiff.generate import generate_diff


P1_JSON = '/home/dima/python-project-50/gendiff/tests/fixtures/file1.json'
P2_JSON = '/home/dima/python-project-50/gendiff/tests/fixtures/file2.json'
P1_YAML = '/home/dima/python-project-50/gendiff/tests/fixtures/file1.yaml'
P2_YAML = '/home/dima/python-project-50/gendiff/tests/fixtures/file2.yaml'
PATH_STYLISH = '/home/dima/python-project-50/gendiff/tests/fixtures/result_stylish.txt'
PATH_PLAIN = '/home/dima/python-project-50/gendiff/tests/fixtures/result_plain.txt'

OPTIONS = [
    (P1_JSON, P2_JSON, 'stylish', PATH_STYLISH),
    (P1_YAML, P2_YAML, 'stylish', PATH_STYLISH),
    (P1_JSON, P2_JSON, 'plain', PATH_PLAIN),
    (P1_YAML, P2_YAML, 'plain', PATH_PLAIN),
]

@pytest.mark.parametrize("path1, path2, format, path_check_file", OPTIONS)
def test_generate_diff(path1, path2, format, path_check_file):
    res = generate_diff(path1, path2, format)

    with open(path_check_file) as check_file:
        assert res == check_file.read()
