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

# old1 = {
#     "k_unchanged": "world",
#     "k_deleted": True,
#     "k_nested": {
#         "k_count": {
#             'k_next': 5
#         }
#     },
#     'k_changed': 'cat'
#     }
#
#
# new1 = {
#     "k_unchanged": "world",
#     "k_nested": {
#         "k_count": 5
#     },
#     'k_changed': 'dog',
#     'k_added': 'boom',
#     'k_added2': 'bom'
# }
#
# old2 = {
#   "host": "hexlet.io",
#   "timeout": 50,
#   "proxy": "123.234.53.22",
#   "follow": False
# }
#
# new2 = {
#   "timeout": 20,
#   "verbose": True,
#   "host": "hexlet.io"
# }
#
# print(get_diff(old1, new1))
#
# print(get_diff(old2, new2))
#
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
