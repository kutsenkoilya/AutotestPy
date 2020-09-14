"""
Task - check how many smiles ':)' will be printed when following code executes

run as:
pytest -s .\04_pytest_fixtures.py

"""

import pytest

@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")

@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")

@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")

class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        print('1')

    def test_second_smiling_faces(self, prepare_faces):
        print('2')