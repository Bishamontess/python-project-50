from gendiff.differ import get_diff
from gendiff.parser import parse_data
from gendiff.formatter.formatter import format_output
from gendiff.parser import get_data_and_format
from gendiff.formatter.formatter import DEFAULT_FORMAT


def generate_diff(first_path, second_path, style=DEFAULT_FORMAT):
    first_data, first_format = get_data_and_format(first_path)
    second_data, second_format = get_data_and_format(second_path)
    diff = get_diff(
        parse_data(first_data, first_format),
        parse_data(second_data, second_format),
    )
    return format_output(diff, style)
