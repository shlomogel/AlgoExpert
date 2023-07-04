import pytest
from time import time
import timeit


@pytest.mark.parametrize('array, targetSum, expect', [([12, 3, 1, 2, -6, 5, -8, 6], 0, [[-8, 2, 6],[-8, 3, 5],[-6, 1, 5]])])
def test_three_number_sum(array, targetSum,expect):
    res = []
    t1 = timeit.default_timer()
    for a in range(len(array)):
        for b in range(a+1, len(array)):
            for c in range(b+1, len(array)):
                if array[a] + array[b] + array[c] == targetSum:
                    res.append(sorted([array[a], array[b], array[c]]))
    res.sort()
    print(timeit.default_timer()-t1)
    assert expect == res


@pytest.mark.parametrize('array, targetSum, expect', [([12, 3, 1, 2, -6, 5, -8, 6], 0, [[-8, 2, 6],[-8, 3, 5],[-6, 1, 5]])])
def test_three_number_sum1(array: list, targetSum: int ,expect: list[list[int]]):
    res = []
    t1 = timeit.default_timer()
    array.sort()
    for a in range(len(array)):
        for b in range(a+1, len(array)):
            for c in range(b+1, len(array)):
                if array[a] + array[b] + array[c] == targetSum:
                    res.append(sorted([array[a], array[b], array[c]]))
    res.sort()
    print(timeit.default_timer()-t1)
    assert expect == res

from itertools import combinations

@pytest.mark.parametrize('array, targetSum, expect', [([12, 3, 1, 2, -6, 5, -8, 6], 0, [[-8, 2, 6],[-8, 3, 5],[-6, 1, 5]])])
def test_three_number_sum2(array: list, targetSum: int ,expect: list[list[int]]):
    # res = []
    t1 = timeit.default_timer()
    array.sort()
    res = [ sorted(p) for p in combinations(array, 3) if sum(p)==targetSum]
    print(timeit.default_timer()-t1)
    assert True