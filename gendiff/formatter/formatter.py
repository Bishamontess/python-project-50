from gendiff.formatter.stylish import stylish_output
from gendiff.formatter.plain import output_plain
from gendiff.formatter.json import output_json


def format_output(diff, style):
    if style == 'stylish':
        return stylish_output(diff)
    if style == 'plain':
        return output_plain(diff)
    if style == 'json':
        return output_json(diff)
