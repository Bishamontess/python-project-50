from gendiff.cli import get_args
from gendiff.generate_diff import generate_diff


def main():
    first_path, second_path, style = get_args()
    diff = generate_diff(first_path, second_path, style)
    print(diff)


if __name__ == '__main__':
    main()
