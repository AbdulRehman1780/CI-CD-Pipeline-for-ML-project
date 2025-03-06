import pytest

# Function to be tested
def reverse_string(s):
    return s[::-1]

# Unit test
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""

if __name__ == "__main__":
    pytest.main()
