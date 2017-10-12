import pytest

# List all Python .ipynb files
import python as nb

# Define tests as functions beginning with "test_"
def test_expect_equal():
    assert nb.notebook_output == 2

def test_expect_error():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0

def this_wont_be_tested():
    assert nb.notebook_output == 1
