from gendiff.formatter.stylish import stylish_output
from gendiff.formatter.plain import plain_output
from gendiff.formatter.json import json_output


def format_output(diff, style):
    if style == 'stylish':
        return stylish_output(diff)
    elif style == 'plain':
        return plain_output(diff)
    elif style == 'json':
        return json_output(diff)
