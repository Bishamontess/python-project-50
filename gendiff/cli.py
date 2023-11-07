import argparse
from gendiff.generate_diff import DEFAULT_FORMAT


def get_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description="Compares two configuration files and shows a difference."
        )
    parser.add_argument(
        "first_file", help='path to first file')
    parser.add_argument("second_file", help='path to second file')
    parser.add_argument(
        '-f',
        '--format',
        help="set format of output",
        metavar="FORMAT",
        default=DEFAULT_FORMAT,
        )
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
