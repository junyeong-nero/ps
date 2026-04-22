

from typing import List

class BIT:
    """Fenwick Tree for prefix sums."""
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        """Add delta at position idx (0‑based)."""
        i = idx + 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def sum(self, idx: int) -> int:
        """Prefix sum of [0 .. idx] (inclusive)."""
        i = idx + 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_sum(self, left: int, right: int) -> int:
        """Sum of elements in [left, right] (inclusive)."""
        if left > right:
            return 0
        res = self.sum(right)
        if left > 0:
            res -= self.sum(left - 1)
        return res


class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # Precompute depth for each element
        def depth_of(x: int) -> int:
            steps = 0
            while x != 1:
                x = x.bit_count()
                steps += 1
            return steps

        # Initialize depths and BITs for each possible k (0..5)
        depth = [0] * n
        bits = [BIT(n) for _ in range(6)]   # index by k

        for i, val in enumerate(nums):
            d = depth_of(val)
            depth[i] = d
            bits[d].add(i, 1)

        answers = []
        for q in queries:
            if q[0] == 1:          # query type 1
                _, l, r, k = q
                ans = bits[k].range_sum(l, r)
                answers.append(ans)
            else:                  # query type 2
                _, idx, val = q
                old_d = depth[idx]
                new_d = depth_of(val)
                if old_d != new_d:
                    bits[old_d].add(idx, -1)
                    bits[new_d].add(idx, 1)
                    depth[idx] = new_d
                # always update the stored value
                nums[idx] = val

        return answers
