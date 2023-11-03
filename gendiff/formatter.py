import itertools
from gendiff.differ import (
    ADDED,
    CHANGED,
    NESTED,
    NEW_VALUE,
    OLD_VALUE,
    DELETED,
    STATE,
    UNCHANGED,
    VALUE,
)
# def to_str():
#     pass
#
#
# def to_format():
#     lines = []
#     step = 4
#
#     def _walk(node, depth):
#         if not isinstance(node, dict):
#             return f'{node}'
#         for key, value in node.items():
#             val = _walk(value, depth + 1)
#             line = f'{}{key}: {val}'
#             lines.append(line)
#         result = itertools.chain('{', lines, [count * replacer + '}'])
#         return '\n'.join(result)
#
#     return _walk(diff, 0)
#
# def output_stylish(diff):
#
#
#
# def output_plain(diff):
#     pass
#
#
# def output_json(diff):
#     pass
#
#
# def format_output(diff, style):
#     if style == 'stylish':
#         return output_stylish(diff)
#     if style == 'plain':
#         return output_plain(diff)
#     if style == 'json':
#         return output_json(diff)
#



nested = {'nested': {'state': 'nested', 'value': {'count': {'state': 'changed', 'old_value': {'next': 5}, 'new_value': 5}}}, 'changed': {'state': 'changed', 'old_value': 'cat', 'new_value': 'dog'}, 'unchanged': {'state': 'unchanged', 'value': 'world'}, 'deleted': {'state': 'deleted', 'value': True}, 'added': {'state': 'added', 'value': 'boom'}}



print(to_format(nested))
