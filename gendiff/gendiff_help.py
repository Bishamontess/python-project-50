import argparse
from gendiff.generate_diff import generate_diff


def gendiff_help():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format',
                        metavar="FORMAT",
                        help="set format of output")
    args = parser.parse_args()
    make_diff = generate_diff(args.first_file, args.second_file)
    print(make_diff)
