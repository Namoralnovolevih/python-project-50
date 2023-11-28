import pytest
from gendiff.generate import generate_diff


P1_JSON = 'tests/fixtures/file1.json'
P2_JSON = 'tests/fixtures/file2.json'
P1_YAML = 'tests/fixtures/file1.yaml'
P2_YAML = 'tests/fixtures/file2.yaml'
PATH_STYLISH = 'tests/fixtures/result_stylish.txt'
PATH_PLAIN = 'tests/fixtures/result_plain.txt'
PATH_JSON = 'tests/fixtures/result_json.txt'

OPTIONS = [(P1_JSON, P2_JSON, 'stylish', PATH_STYLISH),
           (P1_JSON, P2_JSON, 'plain', PATH_PLAIN),
           (P1_JSON, P2_JSON, 'json', PATH_JSON),
           (P1_YAML, P2_YAML, 'stylish', PATH_STYLISH),
           (P1_YAML, P2_YAML, 'plain', PATH_PLAIN),
           (P1_YAML, P2_YAML, 'json', PATH_JSON),
           ]


@pytest.mark.parametrize("path1, path2, format, path_check_file", OPTIONS)
def test_generate_diff(path1, path2, format, path_check_file):
    res = generate_diff(path1, path2, format)

    with open(path_check_file) as check_file:
        assert res == check_file.read()
