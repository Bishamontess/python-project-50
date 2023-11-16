import json
import os
import pytest

from gendiff.parser import parse_data, get_data_and_format
from gendiff.generate_diff import generate_diff
from gendiff.differ import get_diff


def get_fixture_path(file_name, directory):
    return os.path.join('tests', 'fixtures', directory, file_name)


@pytest.mark.parametrize(
    'first_file, second_file, directory, style, output',
    [
        pytest.param('file1.json', 'file2.json', 'plain', 'stylish',
                     'plain.txt', id='plain_files_default_out'
                     ),
        pytest.param('file1.json', 'file2.yml', 'nested', 'stylish',
                     'stylish_diff.txt', id='nested_files_default_out'
                     ),
        pytest.param('file1.yaml', 'file2.json', 'nested', 'plain',
                     'plain_diff.txt', id='nested_files_plain_out'
                     ),
    ],
)
def test_gendiff_text_output(first_file, second_file, directory, style, output):
    file1_path = get_fixture_path(first_file, directory)
    file2_path = get_fixture_path(second_file, directory)
    with open(get_fixture_path(output, directory), 'r') as f:
        expected = f.read().strip()
    assert generate_diff(file1_path, file2_path, style) == expected


@pytest.mark.parametrize(
    'first_file, second_file, directory, style',
    [('file1.json', 'file2.yml', 'nested', 'json')],
)
def test_gendiff_json_output(first_file, second_file, directory, style):
    file1_path = get_fixture_path(first_file, directory)
    file2_path = get_fixture_path(second_file, directory)
    data1, extension1 = get_data_and_format(file1_path)
    data2, extension2 = get_data_and_format(file2_path)
    diff = get_diff(
        parse_data(data1, extension1),
        parse_data(data2, extension2)
    )
    json_diff = generate_diff(file1_path, file2_path, style)
    assert json.loads(json_diff) == diff
