import math
import random
from typing import List

"""
In the worst case, this runs in O(sqrt(N)).
"""


def crystal_breaks(breaks: List[bool]) -> int:
    """
    You have two crystal balls and are standing on top of a building
    with N floors. Given a list of booleans of length N that represent
    whether or not the ball breaks if you drop one from that floor, return
    the first floor at which a ball will break if you drop it. Remember that
    there are only two balls, meaning that you can only traverse a True value
    in the list at most twice.
    """
    N = len(breaks)
    step = math.floor(math.sqrt(N))
    for i in range(0, N, step):
        if breaks[i]:
            for j in range(i - step, i):
                if breaks[j]:
                    return j
    return -1


class Test:
    def __init__(self, N):
        breaks_at = random.randint(0, N)
        print(f"The ball should break at floor {breaks_at}.")
        breaks = [False] * breaks_at + [True] * (N - breaks_at)
        broke_at = crystal_breaks(breaks)
        print(f"The ball broke at floor {broke_at}.")
        print(f"Test {"passed" if broke_at == breaks_at else "failed"}")
        assert broke_at == breaks_at

if __name__ == "__main__":
    Test(100)
    Test(1000)
    Test(10000)
    Test(10000000)