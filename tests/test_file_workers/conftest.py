import pytest


# fixture в pytest

@pytest.fixture(autouse=True)
def clean_text_file():
    with open('testfile.txt', 'w'):
        pass
