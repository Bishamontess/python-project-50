from gendiff import gendiff_help
from gendiff.generate_diff import generate_diff


def main():
    gendiff_help.gendiff_help()
    diff = generate_diff("/home/bishamon/Documents/file1.json", "/home/bishamon/Documents/file2.json")
    print(diff)


if __name__ == '__main__':
    main()
