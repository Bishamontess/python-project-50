import json


def make_diff_string(result_json):
    jsons_diff = ''
    for_del_list = ["{", "}", '"', "'"]
    for i in result_json:
        if i not in for_del_list:
            jsons_diff += i
        else:
            continue
    jsons_diff = jsons_diff.replace(", ", "\n")
    jsons_diff = jsons_diff.replace("^", " ")
    jsons_diff_result = (("{" + "\n" + jsons_diff + "\n" +
                          "}" + "\n"))
    return jsons_diff_result


def generate_diff(path_to_json1, path_to_json2):
    dict1 = json.load(open(path_to_json1))
    dict2 = json.load(open(path_to_json2))
    all_keys = list(set(list(dict1.keys()) + list(dict2.keys())))
    all_keys.sort()

    result = {}
    for key in all_keys:
        if key in dict1 and key in dict2:
            if dict1.get(key) == dict2.get(key):
                special_key = f'  ^ {key}'
                result[special_key] = dict1[key]
            else:
                key_1 = f'  - {key}'
                key_2 = f'  + {key}'
                result[key_1] = dict1[key]
                result[key_2] = dict2[key]
        if key not in dict1:
            new_key = f'  + {key}'
            result[new_key] = dict2[key]
        if key not in dict2:
            new_key = f'  - {key}'
            result[new_key] = dict1[key]
    result_json = json.dumps(result)
    jsons_diff = make_diff_string(result_json)
    return jsons_diff
