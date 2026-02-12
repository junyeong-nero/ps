class SegmentTree:

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self._build(1, 0, self.n - 1, arr)
        
        for i in range(self.n):
            self.tree[i + n] = arr[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, value):
        pos = index + self.n
        while pos:
            self.tree[pos << 1] = self.tree[pos] + self.tree[pos ^ 1]
            pos >>= 1

    def query(self, left, right):
        
        left += self.n
        right += self.n
        res = 0

        while left <= right:
            if left & 1:
                res += self.tree[left]
                left += 1

            if right & 1 == 0:
                right -= 1
                res += self.tree[right]
            
            left >>= 1
            right >>= 1

        return res


class SegmentTreeLazy:

    """
    Segment Tree with Lazy Propagation
    - build from initial array
    - range_add(l, r, val)
    - range_sum(l, r)
    Indices are 0-based and inclusive.
    """

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        if self.n > 0:
            self._build(1, 0, self.n - 1, arr)

    def _build(self, node, start, end, arr):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self._build(node * 2, start, mid, arr)
        self._build(node * 2 + 1, mid + 1, end, arr)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _push(self, node, start, end):
        """Push lazy value down to children (if not a leaf) and apply to this node."""
        if self.lazy[node] != 0:
            add = self.lazy[node]
            self.tree[node] += (end - start + 1) * add
            if start != end:  # not a leaf
                self.lazy[node * 2] += add
                self.lazy[node * 2 + 1] += add
            self.lazy[node] = 0

    def range_add(self, l, r, val):
        if self.n == 0:
            return
        self._range_add(1, 0, self.n - 1, l, r, val)

    def _range_add(self, node, start, end, l, r, val):
        self._push(node, start, end)

        if r < start or end < l:  # no overlap
            return

        if l <= start and end <= r:  # total overlap
            self.lazy[node] += val
            self._push(node, start, end)
            return

        mid = (start + end) // 2
        self._range_add(node * 2, start, mid, l, r, val)
        self._range_add(node * 2 + 1, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def range_sum(self, l, r):
        if self.n == 0:
            return 0
        return self._range_sum(1, 0, self.n - 1, l, r)

    def _range_sum(self, node, start, end, l, r):
        self._push(node, start, end)

        if r < start or end < l:  # no overlap
            return 0

        if l <= start and end <= r:  # total overlap
            return self.tree[node]

        mid = (start + end) // 2
        left_sum = self._range_sum(node * 2, start, mid, l, r)
        right_sum = self._range_sum(node * 2 + 1, mid + 1, end, l, r)
        return left_sum + right_sum


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    st = SegmentTreeLazy(arr)

    print(st.range_sum(1, 3))  # 2+3+4 = 9

    st.range_add(1, 3, 10)     # add 10 to indices 1..3
    print(st.range_sum(1, 3))  # (12+13+14) = 39
    print(st.range_sum(0, 4))  # 1 + 12 + 13 + 14 + 5 = 45

