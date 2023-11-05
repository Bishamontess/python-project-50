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


def make_line(key, value, state, indent):
    view = '{ind}{sign} {key}: {value}'.format
    sign = {
        DELETED: '-',
        ADDED: '+',
        UNCHANGED: ' ',
        NESTED: ' ',
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
        # stylish_diff = '\n'.join(result)
        # return stylish_diff + '\n'
    return _walk(diff, space_count)


def stylish_output(diff, space_count=2):
    step = 4
    inner_step = step // 2
    replacer = ' '

    def _walk(node, depth):
        lines = []

        for key in sorted(node):
            data = node[key]
            state = data[STATE]
            value = data.get(VALUE)

            if state == NESTED:
                value = stylish_output(value, depth + step)

            if state == CHANGED:
                old_value = format_inner(data[OLD_VALUE], depth + inner_step)
                lines.append(make_line(key, old_value, DELETED, depth))
                new_value = format_inner(data[NEW_VALUE], depth + inner_step)
                lines.append(make_line(key, new_value, ADDED, depth))
                continue

            f_value = format_inner(value, depth + inner_step)
            lines.append(make_line(key, f_value, state, depth))

        result = itertools.chain('{', lines, [(depth - inner_step) * replacer +
                                              '}'])
        return '\n'.join(result)
        # stylish_result = '\n'.join(result)
        # return stylish_result + '\n'
    return _walk(diff, space_count)
