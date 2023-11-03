STATE = 'state'
NESTED = 'nested'
ADDED = 'added'
DELETED = 'deleted'
CHANGED = 'changed'
UNCHANGED = 'unchanged'
VALUE = 'value'
OLD_VALUE = 'old_value'
NEW_VALUE = 'new_value'



# def generate_diff(dict1, dict2):
#     dict1 = parse_data(dict1)
#     dict2 = parse_data(dict2)
#
#     all_keys = list(set(list(dict1.keys()) + list(dict2.keys())))
#     all_keys.sort()
#
#     result = {}
#     for key in all_keys:
#         if key in dict1 and key in dict2:
#             if dict1.get(key) == dict2.get(key):
#                 special_key = f'  ^ {key}'
#                 result[special_key] = dict1[key]
#             else:
#                 key_1 = f'  - {key}'
#                 key_2 = f'  + {key}'
#                 result[key_1] = dict1[key]
#                 result[key_2] = dict2[key]
#         if key not in dict1:
#             new_key = f'  + {key}'
#             result[new_key] = dict2[key]
#         if key not in dict2:
#             new_key = f'  - {key}'
#             result[new_key] = dict1[key]
#     result_json = json.dumps(result)
#     jsons_diff = make_diff_string(result_json)
#     return jsons_diff

# def stringify(tree, replacer=" ", spaces_count=1):
#     replacer = replacer * spaces_count
#
#     def walk(node, count):
#         if not isinstance(node, dict):
#             return f'{node}'
#
#         lines = []
#
#         for key, value in node.items():
#             val = walk(value, count + 1)
#             line = f'{replacer * (count + 1)}{key}: {val}'
#             lines.append(line)
#         result = itertools.chain('{', lines, [count * replacer + '}'])
#         return '\n'.join(result)
#     return walk(tree, 0)


def get_diff(old, new):
    diff = {}
    kept = old.keys() & new.keys()
    deleted = old.keys() - new.keys()
    added = new.keys() - old.keys()

    for k_key in kept:
        old_k_value = old[k_key]
        new_k_value = new[k_key]
        if isinstance(old_k_value, dict) and isinstance(new_k_value, dict):
            diff[k_key] = {
                STATE: NESTED,
                VALUE: get_diff(old_k_value, new_k_value)
            }
        elif old_k_value == new_k_value:
            diff[k_key] = {
                STATE: UNCHANGED,
                VALUE: old_k_value
            }
        else:
            diff[k_key] = {
                STATE: CHANGED,
                OLD_VALUE: old_k_value,
                NEW_VALUE: new_k_value
            }

    for d_key in deleted:
        d_value = old1[d_key]
        diff[d_key] = {
            STATE: DELETED,
            VALUE: d_value
        }

    for a_key in added:
        a_value = new[a_key]
        diff[a_key] = {
            STATE: ADDED,
            VALUE: a_value
        }

    return diff



    # result = {}
    # all_keys = dict1.keys() | dict2.keys()
    # for key in all_keys:
    #     if key not in dict1:
    #         result[key] = "added"
    #     elif key not in dict2:
    #         result[key] = "deleted"
    #     elif dict1[key] == dict2[key]:
    #         result[key] = "unchanged"
    #     elif dict1[key] != dict2[key]:
    #         result[key] = "changed"
    # return result


old1 = {
    "unchanged": "world",
    "deleted": True,
    "nested": {
        "count": {
            'next': 5
        }
    },
    'changed': 'cat'
    }


new1 = {
    "unchanged": "world",
    "nested": {
        "count": 5
    },
    'changed': 'dog',
    'added': 'boom'
}


print(get_diff(old1, new1))
