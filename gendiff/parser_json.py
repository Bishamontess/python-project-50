import json


def parser_json(path_to_json1, path_to_json2):
    dict1 = json.load(open(path_to_json1))
    dict2 = json.load(open(path_to_json2))
    return dict1, dict2
