from gendiff.generate_diff import generate_diff


def test_generate_diff():
    expected = open("/home/bishamon/python-project-50/tests/fixtures"
                    "/test_generate_diff/expected.txt").read()
    assert generate_diff(
        "/home/bishamon/python-project-50/tests/"
        "fixtures/test_generate_diff/file1_test.json",
        "/home/bishamon/python-project-50/"
        "tests/fixtures/test_generate_diff/file2_test.json") == expected
    print("Successfully")
