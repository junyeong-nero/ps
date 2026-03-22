from typing import List
from bisect import bisect_left, bisect_right
from collections import defaultdict


class MinMaxSegTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        INF = 10**18
        self.mn = [INF] * (2 * size)
        self.mx = [-INF] * (2 * size)

        for i, x in enumerate(arr):
            self.mn[size + i] = x
            self.mx[size + i] = x

        for i in range(size - 1, 0, -1):
            self.mn[i] = min(self.mn[i << 1], self.mn[i << 1 | 1])
            self.mx[i] = max(self.mx[i << 1], self.mx[i << 1 | 1])

    def query(self, l: int, r: int):
        # inclusive [l, r]
        l += self.size
        r += self.size
        mn = 10**18
        mx = -10**18

        while l <= r:
            if l & 1:
                mn = min(mn, self.mn[l])
                mx = max(mx, self.mx[l])
                l += 1
            if not (r & 1):
                mn = min(mn, self.mn[r])
                mx = max(mx, self.mx[r])
                r -= 1
            l >>= 1
            r >>= 1

        return mn, mx


class PSTNode:
    __slots__ = ("left", "right", "cnt", "sm")

    def __init__(self, left=None, right=None, cnt=0, sm=0):
        self.left = left
        self.right = right
        self.cnt = cnt
        self.sm = sm


def build_empty(lo: int, hi: int) -> PSTNode:
    node = PSTNode()
    if lo != hi:
        mid = (lo + hi) >> 1
        node.left = build_empty(lo, mid)
        node.right = build_empty(mid + 1, hi)
    return node


def update(prev: PSTNode, lo: int, hi: int, idx: int, val: int) -> PSTNode:
    node = PSTNode(prev.left, prev.right, prev.cnt + 1, prev.sm + val)
    if lo == hi:
        return node
    mid = (lo + hi) >> 1
    if idx <= mid:
        node.left = update(prev.left, lo, mid, idx, val)
    else:
        node.right = update(prev.right, mid + 1, hi, idx, val)
    return node


def kth(left_root: PSTNode, right_root: PSTNode, lo: int, hi: int, k: int) -> int:
    # returns compressed index of k-th smallest in (right_root - left_root)
    if lo == hi:
        return lo
    mid = (lo + hi) >> 1
    left_count = right_root.left.cnt - left_root.left.cnt
    if k <= left_count:
        return kth(left_root.left, right_root.left, lo, mid, k)
    return kth(left_root.right, right_root.right, mid + 1, hi, k - left_count)


def prefix_leq_sum_count(
    left_root: PSTNode,
    right_root: PSTNode,
    lo: int,
    hi: int,
    idx: int,
):
    """
    In (right_root - left_root), returns:
    (count of values <= idx, sum of values <= idx)
    """
    if idx < lo:
        return 0, 0
    if hi <= idx:
        return right_root.cnt - left_root.cnt, right_root.sm - left_root.sm

    mid = (lo + hi) >> 1
    c1, s1 = prefix_leq_sum_count(left_root.left, right_root.left, lo, mid, idx)
    c2, s2 = prefix_leq_sum_count(left_root.right, right_root.right, mid + 1, hi, idx)
    return c1 + c2, s1 + s2


class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # 1) remainder array for feasibility check
        rems = [x % k for x in nums]
        rem_tree = MinMaxSegTree(rems)

        # 2) group by remainder
        groups = defaultdict(list)  # rem -> list of (index, normalized_value)
        for i, x in enumerate(nums):
            rem = x % k
            norm = (x - rem) // k
            groups[rem].append((i, norm))

        # 3) build per-group persistent segtree
        group_data = {}
        for rem, items in groups.items():
            positions = [idx for idx, _ in items]
            vals = [v for _, v in items]

            sorted_unique = sorted(set(vals))
            m = len(sorted_unique)
            comp = {v: i for i, v in enumerate(sorted_unique)}

            base = build_empty(0, m - 1)
            roots = [base]
            for v in vals:
                roots.append(update(roots[-1], 0, m - 1, comp[v], v))

            group_data[rem] = (positions, roots, sorted_unique)

        ans = []

        for l, r in queries:
            mn, mx = rem_tree.query(l, r)
            if mn != mx:
                ans.append(-1)
                continue

            rem = mn
            positions, roots, values = group_data[rem]

            left_idx = bisect_left(positions, l)
            right_idx = bisect_right(positions, r)
            length = right_idx - left_idx

            if length <= 1:
                ans.append(0)
                continue

            left_root = roots[left_idx]
            right_root = roots[right_idx]

            # median
            kth_order = (length + 1) // 2
            med_comp_idx = kth(left_root, right_root, 0, len(values) - 1, kth_order)
            med_val = values[med_comp_idx]

            # left part (<= median)
            left_cnt, left_sum = prefix_leq_sum_count(
                left_root, right_root, 0, len(values) - 1, med_comp_idx
            )

            total_cnt = length
            total_sum = right_root.sm - left_root.sm
            right_cnt = total_cnt - left_cnt
            right_sum = total_sum - left_sum

            cost = med_val * left_cnt - left_sum + right_sum - med_val * right_cnt
            ans.append(cost)

        return ans

# from typing import List
# from collections import Counter

# class CounterSegTree:
#     def __init__(self, arr):
#         self.n = len(arr)
#         self.tree = [Counter() for _ in range(2 * self.n)]
#         for i, x in enumerate(arr):
#             self.tree[self.n + i] = Counter({x: 1})
#         for i in range(self.n - 1, 0, -1):
#             self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

#     def query(self, left, right):   # [left, right)
#         left += self.n
#         right += self.n
#         res_left = Counter()
#         res_right = Counter()

#         while left < right:
#             if left & 1:
#                 res_left += self.tree[left]
#                 left += 1
#             if right & 1:
#                 right -= 1
#                 res_right = self.tree[right] + res_right
#             left >>= 1
#             right >>= 1

#         return res_left + res_right


# class Solution:
#     def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
#         # 1) remainder counter tree
#         rems = [x % k for x in nums]
#         rem_tree = CounterSegTree(rems)

#         ans = []

#         for l, r in queries:
#             cnt = rem_tree.query(l, r + 1)

#             # remainder가 2개 이상이면 불가능
#             if len(cnt) != 1:
#                 ans.append(-1)
#                 continue

#             rem = next(iter(cnt.keys()))

#             # 2) 가능한 경우, 정규화된 값들 추출
#             vals = [(nums[i] - rem) // k for i in range(l, r + 1)]
#             vals.sort()

#             m = vals[len(vals) // 2]
#             cost = sum(abs(v - m) for v in vals)
#             ans.append(cost)

#         return ans
