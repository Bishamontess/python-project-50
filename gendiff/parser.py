import json
import yaml

SUPPORTED_FORMATS = {
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
    'json': json.load,
}


def get_file(file_path):
    return open(file_path, 'r')


def get_extension(file_path):
    file_name = file_path.split('/')[-1]
    file_extension = file_name.split('.')[-1]
    if file_extension not in SUPPORTED_FORMATS:
        message = (
            'File "{n}" has wrong format: "{f}". Supported formats: {'
            's}'.format)
        supported = ', '.join(SUPPORTED_FORMATS)
        raise TypeError(message(
            n=file_name,
            f=file_extension,
            s=supported,
        ))
    return file_extension


def parse_data(data, data_format):
    parser = SUPPORTED_FORMATS.get(data_format)
    return parser(data)


def get_data_and_format(source, data=get_file, data_format=get_extension):
    return data(source), data_format(get_extension(source))
