import os
import pytest

# Load all converted Python notebooks
for module in os.listdir(os.path.dirname(__file__)):
    if module[-3:] != '.py':
        continue
    __import__(module[:-3], locals(), globals())
del module

# Run tests
def expect_equal():
    assert notebook_output == 2

def expect_error():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0
