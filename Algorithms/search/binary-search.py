from typing import List


def search(array: List[int], value: int) -> int:
    """
    Returns the index of an occurence of the value in the array.
    It is not guaranteed to be the first occurence.
    If no such element is found, the function returns -1.
    """
    l, r = 0, len(array)
    while l < r:
        middle = l + (r - l) // 2
        if array[middle] == value:
            return middle
        elif array[middle] > value:
            r = middle
        else:
            l = middle + 1
    return -1


def test_search():
    assert search([], 0) == -1
    assert search([1], 1) == 0
    assert search([1, 2, 3, 4, 5], 1) == 0
    assert search([1, 2, 3, 4, 5], 5) == 4
    assert search([1, 2, 3, 4, 5], 3) == 2
    assert search([1, 2, 3, 4, 5], 6) == -1
    assert search([1, 2, 3, 4, 5], -1) == -1
    assert search([1, 2, 3, 4, 5], 0) == -1
    assert search([1, 2, 3, 4, 5], 2.5) == -1
    assert search([1, 2, 3, 4, 5], 3.5) == -1
    assert search([1, 2, 3, 4, 5], 4.5) == -1
    assert search([1, 2, 3, 4, 5], 1.5) == -1
    assert search([1, 2, 3, 4, 5], 2) == 1
    assert search([1, 2, 3, 4, 5], 3) == 2
    assert search([1, 2, 3, 4, 5], 4) == 3
    assert search([1, 2, 3, 4, 5], 5) == 4
    assert search([1, 2, 3, 4, 5], 6) == -1
    assert search([1, 2, 3, 4, 5], -1) == -1
    assert search([1, 2, 3, 4, 5], 0)


test_search()
