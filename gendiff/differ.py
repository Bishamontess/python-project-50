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
                'state': 'nested',
                'value': get_diff(old_k_value, new_k_value)
            }
        elif old_k_value == new_k_value:
            diff[k_key] = {
                'state': 'unchanged',
                'value': old_k_value
            }
        else:
            diff[k_key] = {
                'state': 'changed',
                'old_value': old_k_value,
                'new_value': new_k_value
            }

    for d_key in deleted:
        d_value = old[d_key]
        diff[d_key] = {
            'state': 'deleted',
            'value': d_value
        }

    for a_key in added:
        a_value = new[a_key]
        diff[a_key] = {
            'state': 'added',
            'value': a_value
        }

    return diff
