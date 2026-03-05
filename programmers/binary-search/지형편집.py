from bisect import bisect_left
from itertools import chain


def solution(land, P, Q):
    # Flatten + sort heights
    arr = sorted(chain.from_iterable(land))
    n = len(arr)

    # Prefix sums: prefix[i] = sum(arr[:i])
    prefix = [0] * (n + 1)
    for i, v in enumerate(arr, 1):
        prefix[i] = prefix[i - 1] + v

    total = prefix[n]

    def cost(h: int) -> int:
        """
        Cost to make all cells height h:
        - raise values < h with cost P per unit
        - lower values > h with cost Q per unit
        """
        i = bisect_left(arr, h)  # first index with arr[i] >= h

        # Raise arr[0:i] up to h
        raise_units = h * i - prefix[i]

        # Lower arr[i:n] down to h
        lower_units = (total - prefix[i]) - h * (n - i)

        return raise_units * P + lower_units * Q

    lo, hi = arr[0], arr[-1]

    # Discrete convex minimization (unimodal over integer heights)
    while lo < hi:
        mid = (lo + hi) // 2
        if cost(mid) <= cost(mid + 1):
            hi = mid
        else:
            lo = mid + 1

    return cost(lo)
