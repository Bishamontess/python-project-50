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
    return '{0}'.format(value)


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
