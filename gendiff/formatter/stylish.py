import itertools


def to_str(value):
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return str(value)


def make_line(key, value, state, indent):
    view = '{ind}{sign} {key}: {value}'.format
    sign = {
        'deleted': '-',
        'added': '+',
        'unchanged': ' ',
        'nested': ' ',
    }
    replacer = ' '
    return view(
        ind=replacer * indent,
        sign=sign.get(state),
        key=key,
        value=value
    )


def format_inner(diff, space_count=2):
    view = '{ind}{key}: {value}'.format
    step = 4

    def _walk(node, depth):
        if not isinstance(node, dict):
            return to_str(node)
        lines = []
        replacer = ' '
        for key, value in node.items():
            lines.append(view(
                ind=replacer * (depth + step),
                key=key,
                value=_walk(value, depth + step)
            ))
        result = itertools.chain('{', lines, [depth * replacer + '}'])
        return '\n'.join(result)

    return _walk(diff, space_count)


def stylish_output(diff, space_count=2):
    step = 4
    inner_step = step // 2
    replacer = ' '

    def _walk(node, depth):
        lines = []
        for key in sorted(node):
            data = node[key]
            state = data['state']
            value = data.get('value')
            if state == 'nested':
                value = stylish_output(value, depth + step)
            if state == 'changed':
                old_value = format_inner(data['old_value'], depth + inner_step)
                lines.append(make_line(key, old_value, 'deleted', depth))
                new_value = format_inner(data['new_value'], depth + inner_step)
                lines.append(make_line(key, new_value, 'added', depth))
                continue
            f_value = format_inner(value, depth + inner_step)
            lines.append(make_line(key, f_value, state, depth))
        result = itertools.chain('{', lines, [(depth - inner_step)
                                              * replacer + '}'])
        return '\n'.join(result)

    return _walk(diff, space_count)
