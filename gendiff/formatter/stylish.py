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


def to_str(value):
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return str(value)


def make_line(key, value, state, indent='  '):
    view = '{ind}{sign} {key}: {value}'.format
    sign = {
        DELETED: '-',
        ADDED: '+',
        UNCHANGED: ' ',
        NESTED: ' ',
    }

    return view(
        ind=indent,
        sign=sign.get(state),
        key=key,
        value=value
    )


def stylish_output(diff):
    lines = []

    for key in sorted(diff):
        data = diff[key]
        state = data[STATE]
        value = data.get(VALUE)

        if state == DELETED:
            lines.append(make_line(key, to_str(value), DELETED))

        if state == ADDED:
            lines.append(make_line(key, to_str(value), ADDED))

        if state == UNCHANGED:
            lines.append(make_line(key, value, UNCHANGED))

        if state == CHANGED:
            old_v = data[OLD_VALUE]
            new_v = data[NEW_VALUE]
            lines.append(make_line(key, to_str(old_v), DELETED))
            lines.append(make_line(key, to_str(new_v), ADDED))
            continue

    result = itertools.chain('{', lines, '}')
    result = '\n'.join(result)
    return result + '\n'

#
# nested = {
#     'k_unchanged': {
#         'state': 'unchanged',
#         'value': 'world'},
#     'k_changed': {
#         'state': 'changed',
#         'old_value': 'cat',
#         'new_value': 'dog'
#     },
#     'k_nested': {
#         'state': 'nested',
#         'value': {
#             'k_count': {
#                 'state': 'changed',
#                 'old_value': {
#                     'k_next': 5
#                 },
#                 'new_value': 5
#             }
#         }
#     },
#     'k_deleted': {
#         'state': 'deleted',
#         'value': True
#     },
#     'k_added2': {
#         'state': 'added',
#         'value': 'bom'
#     },
#     'k_added': {
#         'state': 'added',
#         'value': 'boom'
#     }
# }
#
# plain = {
#     'host': {
#         'state': 'unchanged',
#         'value': 'hexlet.io'
#     },
#     'timeout': {
#         'state': 'changed',
#         'old_value': 50,
#         'new_value': 20
#     },
#     'proxy': {
#         'state': 'deleted',
#         'value': '123.234.53.22'
#     },
#     'follow': {
#         'state': 'deleted',
#         'value': False
#     },
#     'verbose': {
#         'state': 'added',
#         'value': True
#     }
# }
# print(stylish_output(plain))
# print(to_format(nested))


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
#     for key in diff:


# def make_line(key, value, state, indent):
#     view = '{ind}{sign} {key}: {value}'.format
#     signs = {
#         DELETED: '-',
#         ADDED: '+',
#         UNCHANGED: ' ',
#         NESTED: ' ',
#     }
#     replacer = ' '
#     return view(
#         ind=replacer * indent,
#         sign=signs.get(state),
#         key=key,
#         value=value,
#     )
#
#
# def format_value(tree, spaces_count=2):
#     view = '{ind}{key}: {value}'.format
#     step = 4
#
#     def _walk(node, count):
#         if not isinstance(node, dict):
#             return to_str(node)
#
#         line = []
#         replacer = ' '
#
#         for key, value in node.items():
#             line.append(view(
#                 ind=replacer * (count + step),
#                 key=key,
#                 value=_walk(value, count + step),
#             ))
#         result = itertools.chain('{', line, [count * replacer + '}'])
#         return '\n'.join(result)
#     return _walk(tree, spaces_count)
#
#
# def to_format(tree, spaces_count=2):
#     step = 4
#     inner_step = step // 2
#     replacer = ' '
#
#     def _walk(node, count):
#         lines = []
#
#         for key in sorted(node):
#             data = node[key]
#             state = data[STATE]
#             value = data.get(VALUE)
#
#             if state == NESTED:
#                 value = to_format(value, count + step)
#
#             if state == CHANGED:
#                 old_value = format_value(data[OLD_VALUE], count + inner_step)
#                 lines.append(make_line(key, old_value, DELETED, count))
#                 new_value = format_value(data[NEW_VALUE], count + inner_step)
#                 lines.append(make_line(key, new_value, ADDED, count))
#                 continue
#
#             f_value = format_value(value, count + inner_step)
#             lines.append(make_line(key, f_value, state, count))
#
#         result = itertools.chain('{', lines, [(count - inner_step) * replacer
#                                               + '}'])
#         return '\n'.join(result)
#     return _walk(tree, spaces_count)
