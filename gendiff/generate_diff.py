import json


def generate_diff(path_to_json1, path_to_json2):
    dict1 = json.load(open(path_to_json1))
    dict2 = json.load(open(path_to_json2))
    list_all_keys = list(dict1.keys()) + list(dict2.keys())
    all_keys = set(list_all_keys)
    result = ''
    for key in all_keys:
        if key in dict1 and key in dict2:
            if dict1.get(key) == dict2.get(key):
                string = f"{key}: {dict1[key]}\n"
                result += string
            else:
                string = f"- {key}: {dict1[key]}\n+ {key}: {dict2[key]}\n"
                result += string
        if key not in dict1:
            string = f"+ {key}: {dict2[key]}\n"
            result += string
        if key not in dict2:
            string = f"- {key}: {dict1[key]}\n"
            result += string
    string_diff = "{" + "\n" + result + "}"
    return string_diff
