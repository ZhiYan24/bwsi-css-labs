"""
tests_1d.py

This module contains unit tests for the two_sum defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test():
    assert two_sum([2,7,11,15],9) == [0,1]
    assert two_sum([-10,-5,6,13],-4) == [0,2]
    assert two_sum([-18,-14,-8,-3],-22) == [1,2]

if __name__ == "__main__":
    pytest.main()