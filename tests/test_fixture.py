
import pytest

@pytest.fixture
def my_data():
    # Setup: Provide some data
    data = {"key": "value"}
    yield data  # Yield the data to the test
    # Teardown: Cleanup if necessary
    print("Cleaning up my_data")


def test_using_my_data(my_data):
    assert my_data["key"] == "value"