from my_funcs.file_workers import read_from_file


def test_file_workers():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n', 'five\n']
    assert test_data == read_from_file('tests/testfile.txt')