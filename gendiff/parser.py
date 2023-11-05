import json
import yaml


def get_file(file_path):
    return open(file_path, 'r')


def get_extension(file_path):
    file_name = file_path.split('/')[-1]
    file_extension = file_name.split('.')[-1]
    return file_extension


def parse_data(data, data_format):
    if data_format == 'yaml' or 'yml':
        return yaml.safe_load(data)
    elif data_format == 'json':
        return json.load(data)


def get_data_and_format(source, data=get_file, data_format=get_extension):
    return data(source), data_format(get_extension(source))
