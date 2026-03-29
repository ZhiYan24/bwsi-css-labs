"""
tests_1c.py

This module contains unit tests for the max_subarray function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([-5,-3,-2,0,-4,-3,-1]) == 0
    assert max_subarray_sum([1,2,3,4,5,6,7,8,9,-60,50]) == 50

if __name__ == "__main__":
    pytest.main()