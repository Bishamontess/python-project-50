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
        'deleted': 'was removed',
        'changed': 'was updated.',
        'added': 'was added with value:',
    }

    if state == 'deleted':
        line = f"{first_word} '{path}' {options[state]}"

    elif state == 'added':
        line = f"{first_word} '{path}' {options[state]} {value}"

    elif state == 'changed':
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
        state = data['state']

        if state == 'nested':
            lines.append(plain_output(data['value'], path))

        if state == 'changed':
            old_val = to_str(data['old_value'])
            new_val = to_str(data['new_value'])
            line = make_line(path, state, old_val, new_val)

        else:
            value = to_str(data['value'])
            line = make_line(path, state, value=value)

        path.pop()
        lines.append(line)

    return '\n'.join(line for line in lines if line)
