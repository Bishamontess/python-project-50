import yaml


def parser_yml(path_to_yaml1, path_to_yaml2):
    dict1 = yaml.safe_load(open(path_to_yaml1))
    dict2 = yaml.safe_load(open(path_to_yaml2))
    return dict1, dict2
