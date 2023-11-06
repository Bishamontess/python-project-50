STATE = 'state'
NESTED = 'nested'
ADDED = 'added'
DELETED = 'deleted'
CHANGED = 'changed'
UNCHANGED = 'unchanged'
VALUE = 'value'
OLD_VALUE = 'old_value'
NEW_VALUE = 'new_value'


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
        d_value = old[d_key]
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
# old = {
#     "host": "hexlet.io",
#     "timeout": 50,
#     "proxy": "123.234.53.22",
#     "follow": False,
#     'k_nested': {
#         'k_nest': '',
#         'k_nested': {
#             'deep_key': 'deep_value'
#         }
#     }
# }
#
# new = {
#     "timeout": 20,
#     "verbose": True,
#     "host": "hexlet.io",
#     'k_nested': {
#             'k_nest': 'changed_v',
#             'k_nested': {
#                 'deep_key': 'another_deep_value'
#             }
#     }
# }
#
#
# print(get_diff(old, new))
# old = {
#     "common": {
#         "setting1": "Value 1",
#         "setting2": 200,
#         "setting3": True,
#         "setting6": {
#             "key": "value",
#             "doge": {
#                 "wow": ""
#             }
#         }
#     },
#     "group1": {
#         "baz": "bas",
#         "foo": "bar",
#         "nest": {
#             "key": "value"
#         }
#     },
#     "group2": {
#         "abc": 12345,
#         "deep": {
#             "id": 45
#         }
#     }
# }
# new = {
#     "common": {
#         "follow": False,
#         "setting1": "Value 1",
#         "setting3": 'null',
#         "setting4": "blah blah",
#         "setting5": {
#             "key5": "value5"
#         },
#         "setting6": {
#             "key": "value",
#             "ops": "vops",
#             "doge": {
#                 "wow": "so much"
#             }
#         }
#     },
#     "group1": {
#         "foo": "bar",
#         "baz": "bars",
#         "nest": "str"
#     },
#     "group3": {
#         "deep": {
#             "id": {
#                 "number": 45
#             }
#         },
#         "fee": 100500
#     }
# }
# print(get_diff(old, new))
