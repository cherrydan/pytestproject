from my_funcs.create_test_data import create_test_data
from my_funcs.file_workers import read_from_file


def test_file_append():
    test_data = ['one\n', 'two\n', 'three\n']
    create_test_data(test_data)
    assert test_data == read_from_file('testfile.txt')


def test_file_append2():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n', 'five\n']
    create_test_data(test_data)
    assert test_data == read_from_file('testfile.txt')
