import json
import yaml


def get_data(file_path):
    file_name = file_path.split('/')[-1]
    file_extension = file_name.split('.')[-1]
    if file_extension == 'yaml' or 'yml':
        return yaml.safe_load(open(file_path))
    elif file_extension == 'json':
        return json.load(open(file_path))
