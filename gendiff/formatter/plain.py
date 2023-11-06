from gendiff.differ import (ADDED, CHANGED, NESTED, OLD_VALUE, NEW_VALUE,
                            STATE, VALUE, DELETED)


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"


def make_line(path, state, old=None, new=None, value=None):
    first_word = 'Property'
    path = '.'.join(path)

    options = {
        DELETED: 'was removed',
        CHANGED: 'was updated.',
        ADDED: 'was added with value:',
    }

    if state == DELETED:
        line = f"{first_word} '{path}' {options[state]}"

    elif state == ADDED:
        line = f"{first_word} '{path}' {options[state]} {value}"

    elif state == CHANGED:
        line = (f"{first_word} '{path}' {options[state]} From {old} to"
                f" {new}")
    else:
        line = ''
    return line


def plain_output(diff, path=None):
    if path is None:
        path = []
    lines = []
    for key in sorted(diff):
        path.append(key)
        data = diff[key]
        state = data[STATE]

        if state == NESTED:
            lines.append(plain_output(data[VALUE], path))

        if state == CHANGED:
            old_val = to_str(data[OLD_VALUE])
            new_val = to_str(data[NEW_VALUE])
            line = make_line(path, state, old_val, new_val)

        else:
            value = to_str(data[VALUE])
            line = make_line(path, state, value=value)

        path.pop()
        lines.append(line)

    return '\n'.join(line for line in lines if line)
# dif = {
#     'common': {
#         'state': 'nested',
#         'value': {'setting6': {'state': 'nested', 'value': {
#             'key': {'state': 'unchanged', 'value': 'value'},
#             'doge': {'state': 'nested', 'value': {
#                 'wow': {'state': 'changed', 'old_value': '',
#                         'new_value': 'so much'}}},
#             'ops': {'state': 'added', 'value': 'vops'}}},
#                   'setting3': {'state': 'changed', 'old_value': True,
#                                'new_value': 'null'},
#                   'setting1': {'state': 'unchanged', 'value': 'Value 1'},
#                   'setting2': {'state': 'deleted', 'value': 200},
#                   'setting5': {'state': 'added', 'value': {'key5': 'value5'}},
#                   'setting4': {'state': 'added', 'value': 'blah blah'},
#                   'follow': {'state': 'added', 'value': False}}},
#     'group1': {'state': 'nested', 'value': {
#         'nest': {'state': 'changed', 'old_value': {'key': 'value'},
#                  'new_value': 'str'},
#         'foo': {'state': 'unchanged', 'value': 'bar'},
#         'baz': {'state': 'changed', 'old_value': 'bas', 'new_value':
#         'bars'}}},
#     # 'group2': {'state': 'deleted', 'value': {'abc': 12345, 'deep': {
#     'id': 45}}},
#     # 'group3': {'state': 'added',
#     #            'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
# }
#
#
# print(plain_output(dif))
