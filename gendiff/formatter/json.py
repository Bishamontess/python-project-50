import json


def json_output(diff):
    return json.dumps(diff, sort_keys=True)
