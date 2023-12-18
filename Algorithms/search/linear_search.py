from typing import List


def search(array: List[int], value: int) -> int:
    """
    Returns the index of the first occurence of the value in the array.
    If no such element is found, the function returns -1.
    """
    i = 0
    while i < len(array):
        if array[i] == value:
            return i
        i += 1
    return -1
