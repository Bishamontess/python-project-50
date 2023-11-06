from gendiff.formatter.stylish import stylish_output
from gendiff.formatter.plain import plain_output
from gendiff.formatter.json import json_output


DEFAULT_FORMAT = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def format_output(diff, style):
    if style == DEFAULT_FORMAT:
        return stylish_output(diff)
    if style == PLAIN:
        return plain_output(diff)
    if style == JSON:
        return json_output(diff)
