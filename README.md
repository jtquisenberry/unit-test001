# unit-test001


# Test Framework

## `pytest` vs. `unittest`

* __Compatibility:__ The `pytest` test runner is compatible with `unittest` tests.
* __Simplicity:__ Pytest tests can be written as simple functions, but `unittest` tests must inherit from `unittest.TestCase`.
* __Fixtures:__ Pytest fixtures are more powerful and flexible than Unittest's `setUp()` and `tearDown()` methods.
* __Parameterization:__ Pytest allows running the same tests repeatedly with different input data.
* __Plug-ins:__ Pytest supports third-party plug-ins. For example `pytest-order` allows controlling the order in which tests are performed.


# Installing `pytest`

```shell
pip install pytest
```

# Running `pytest`

## PyCharm

Running `pytest` tests in PyCharm or another IDE provides rich reporting options.

## Command Line

To run `pytest` on a given directory and its subdirectories, do the following:

* Activate the virtual environment where `pytest` is installed.
* Start `pytest`, specifying the target directory as an argument.

```shell
> pytest <target directory>
```

_Example_

```shell
(v3124) PS D:\Development\git\unit-test001> pytest tests
================================ test session starts ================================
platform win32 -- Python 3.12.4, pytest-8.4.2, pluggy-1.6.0
rootdir: D:\Development\git\unit-test001
plugins: anyio-4.4.0
collected 7 items                                                                    

tests\arithmetic\add_test.py .                                                 [ 14%]
tests\arithmetic\test_add.py .                                                 [ 28%]
tests\minio\test_minio.py ....                                                 [ 85%]
tests\test_fixture.py .                                                        [100%]

================================= 7 passed in 0.27s =================================
```

# Test Discovery

## File Naming

Pytest looks for files named like `test_*.py` or `*_test.py`.

## Functions and Class Naming

Pytest runs tests on functions beginning with `test_` and methods within classes begging with `Test`.

## Directories

Pytest recursively searches through directories, starting with the specified directory.

# `pytest` Tests

## The `assert` Keyword

```python
assert True
```

```python
expected = 1
actual = 1
assert expected == actual
```

```python
return_value = None
assert return_value is None
```

## Testing Exception Types

```python
import pytest
with pytest.raises(Exception) as excinfo:
    # Call a function that raises an `Exception` or an object 
    # that inherits from `Exception`.
    ...
```

```python
from minio import S3Error
import pytest
with pytest.raises(S3Error) as excinfo:
    # Call a function that raises `minio.S3Error`.
    ...
```

# `pytest` Fixtures

```python
import os
import tempfile
import pytest

@pytest.fixture
def my_fixture():
    """
    A fixture that creates a temporary file for testing and cleans it up afterward.
    """
    # Setup: Create a temporary file
    fd, path = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, 'w') as f:
        f.write("This is temporary test data.")
    print(f"\nSetup: Created temporary file at: {path}")

    # Yield the resource (the path to the temporary file) to the test function
    yield path

    # Teardown: Clean up the temporary file
    os.remove(path)
    print(f"Teardown: Removed temporary file at: {path}")
```

```python
# test_example.py
def test_read_temp_file(temp_file_fixture):
    """
    A test that uses the temp_file_fixture to read data from the temporary file.
    """
    file_path = temp_file_fixture
    with open(file_path, 'r') as f:
        content = f.read()
    assert "temporary test data" in content
    print(f"Test: Read content from {file_path}")

def test_another_use_of_temp_file(temp_file_fixture):
    """
    Another test demonstrating the use of the same fixture.
    """
    file_path = temp_file_fixture
    with open(file_path, 'a') as f:
        f.write("\nAppended more data.")
    with open(file_path, 'r') as f:
        content = f.read()
    assert "Appended more data" in content
    print(f"Test: Appended and verified content in {file_path}")
```