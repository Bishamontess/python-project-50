import json
from gendiff.generate_diff import generate_diff
from gendiff.formatter.formatter import PLAIN
from gendiff.parser import parse_data, get_data_and_format
from gendiff.differ import get_diff
from gendiff.formatter.formatter import JSON


def test_generate_diff_yaml_plain():
    file1 = 'tests/fixtures/plain/file1.yaml'
    file2 = 'tests/fixtures/plain/file2.yml'
    with open('tests/fixtures/plain/plain.txt', 'r') as f:
        output_file = f.read().strip()
    assert generate_diff(file1, file2) == output_file


def test_generate_diff_json_plain():
    file1 = 'tests/fixtures/plain/file1.json'
    file2 = 'tests/fixtures/plain/file2.json'
    with open('tests/fixtures/plain/plain.txt', 'r') as f:
        output_file = f.read().strip()
    assert generate_diff(file1, file2) == output_file


def test_generate_diff_json_nested():
    file1 = 'tests/fixtures/nested/file1.json'
    file2 = 'tests/fixtures/nested/file2.json'
    with open('tests/fixtures/nested/stylish_diff.txt', 'r') as f:
        output_file = f.read().strip()
    assert generate_diff(file1, file2) == output_file


def test_generate_diff_yaml_nested():
    file1 = 'tests/fixtures/nested/file1.yaml'
    file2 = 'tests/fixtures/nested/file2.yml'
    with open('tests/fixtures/nested/stylish_diff.txt', 'r') as f:
        output_file = f.read().strip()
    assert generate_diff(file1, file2) == output_file


def test_generate_diff_plain_output():
    file1 = 'tests/fixtures/nested/file1.yaml'
    file2 = 'tests/fixtures/nested/file2.yml'
    with open('tests/fixtures/nested/plain_diff.txt', 'r') as f:
        output_file = f.read().strip()
    assert generate_diff(file1, file2, PLAIN) == output_file


def test_generate_diff_json_output():
    file1 = 'tests/fixtures/nested/file1.yaml'
    file2 = 'tests/fixtures/nested/file2.yml'
    data1, extension1 = get_data_and_format(file1)
    data2, extension2 = get_data_and_format(file2)
    diff = get_diff(
        parse_data(data1, extension1),
        parse_data(data2, extension2)
    )
    json_diff = generate_diff(file1, file2, JSON)
    assert json.loads(json_diff) == diff
