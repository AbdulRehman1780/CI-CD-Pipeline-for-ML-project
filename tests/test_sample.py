import pytest

# Function to be tested
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Unit tests
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 4) == 6
    assert subtract(0, 1) == -1

if __name__ == "__main__":
    pytest.main()
