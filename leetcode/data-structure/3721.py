from typing import List


class SegmentTree:
    def __init__(self, n: int):
        # 반복문 기반 Lazy Segment Tree.
        # 각 노드는 자신이 담당하는 구간의 [최솟값, 최댓값]을 들고 있어서
        # target 값이 이 구간에 "존재할 가능성"이 있는지 빠르게 판단할 수 있다.
        size = 1 << ((n - 1).bit_length() + 1)
        self.base = size >> 1
        self.min_tree = [0] * size
        self.max_tree = [0] * size
        self.lazy = [0] * self.base

    def _apply(self, node: int, delta: int) -> None:
        # node가 담당하는 구간 전체에 delta를 더한다.
        # 내부 노드라면 아직 자식에게 안 내린 값은 lazy에 보관한다.
        self.min_tree[node] += delta
        self.max_tree[node] += delta
        if node < self.base:
            self.lazy[node] += delta

    def _pull(self, node: int) -> None:
        # 리프/하위 노드 변경 후 부모 방향으로 min/max 정보를 다시 계산한다.
        while node > 1:
            node >>= 1
            left = node << 1
            right = left | 1
            self.min_tree[node] = min(self.min_tree[left], self.min_tree[right])
            self.max_tree[node] = max(self.max_tree[left], self.max_tree[right])
            if self.lazy[node]:
                self.min_tree[node] += self.lazy[node]
                self.max_tree[node] += self.lazy[node]

    def range_add(self, left: int, right: int, delta: int) -> None:
        # [left, right] 구간의 모든 상태값에 delta를 더한다.
        left += self.base
        right += self.base
        left0, right0 = left, right

        while left <= right:
            if left & 1:
                self._apply(left, delta)
                left += 1
            if right & 1 == 0:
                self._apply(right, delta)
                right -= 1
            left >>= 1
            right >>= 1

        self._pull(left0)
        self._pull(right0)

    def first_index_containing(self, target: int) -> int:
        # 값이 target일 수 있는 가장 왼쪽 인덱스를 찾는다.
        # lazy 값이 남아 있으면 내려가면서 즉시 반영(push)한다.
        node = 1
        while node < self.base:
            if self.lazy[node]:
                self._apply(node << 1, self.lazy[node])
                self._apply((node << 1) | 1, self.lazy[node])
                self.lazy[node] = 0

            node <<= 1
            if not (self.min_tree[node] <= target <= self.max_tree[node]):
                node |= 1

        return node - self.base


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # i를 오른쪽 끝으로 고정했을 때, 각 시작점 l에 대해
        # state[l] = (#distinct odd in nums[l..i]) - (#distinct even in nums[l..i])
        # 를 관리한다. 균형 구간은 state[l] == 0 인 경우다.
        n = len(nums) + 1
        seg = SegmentTree(n)

        # 값별 마지막 등장 위치(1-indexed).
        last_pos = {}

        # cur은 l=0 관점의 현재 상태값(odd distinct - even distinct).
        cur = 0
        best = 0

        for i, num in enumerate(nums, 1):
            # 홀수는 +1 기여, 짝수는 -1 기여
            delta = 1 if num & 1 else -1

            if num in last_pos:
                # 같은 값이 이미 있었다면,
                # 이전 마지막 등장 위치 이후 구간에 더해졌던 기존 기여를 제거한다.
                seg.range_add(last_pos[num], n - 1, -delta)
                cur -= delta

            # 이번 등장으로 생기는 최신 기여를 반영한다.
            cur += delta
            last_pos[num] = i

            # 시작점 l이 i 이하라면 nums[i]를 포함하게 되므로 해당 구간에 delta 추가.
            seg.range_add(i, n - 1, delta)

            # state[l] == cur 인 가장 이른 l을 찾으면
            # (해당 l에서의 균형 조건 성립) 길이 i-l이 최대가 된다.
            left = seg.first_index_containing(cur)
            best = max(best, i - left)

        return best
