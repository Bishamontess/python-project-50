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
