from typing import List


class ST:
    def __init__(self, n: int) -> None:
        # 세그먼트 트리 저장소 (충분한 크기로 4N 할당)
        self.tree = [0] * (n * 4 + 1)

    def update(self, start: int, end: int, tree_idx: int, query_idx: int) -> None:
        # 현재 구간이 갱신 대상 인덱스를 포함하지 않으면 종료
        if not (start <= query_idx <= end):
            return

        # 리프 노드라면 해당 값의 등장 횟수 1 증가
        if start == end:
            self.tree[tree_idx] += 1
            return

        # 부분 겹침이면 자식으로 내려가 갱신 후 부모 합 갱신
        mid = (start + end) // 2
        self.update(start, mid, tree_idx * 2, query_idx)
        self.update(mid + 1, end, tree_idx * 2 + 1, query_idx)
        self.tree[tree_idx] = self.tree[tree_idx * 2] + self.tree[tree_idx * 2 + 1]

    def query(
        self,
        start: int,
        end: int,
        tree_idx: int,
        query_start: int,
        query_end: int,
    ) -> int:
        # 겹치지 않는 구간
        if query_end < start or end < query_start:
            return 0

        # 완전히 포함되는 구간
        if query_start <= start and end <= query_end:
            return self.tree[tree_idx]

        # 일부만 겹치면 좌/우 자식 결과 합산
        mid = (start + end) // 2
        left_sum = self.query(start, mid, tree_idx * 2, query_start, query_end)
        right_sum = self.query(mid + 1, end, tree_idx * 2 + 1, query_start, query_end)
        return left_sum + right_sum


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 좌표 압축: nums와 2*nums를 함께 압축해 세그먼트 트리 인덱스로 사용
        sorted_candidates = sorted(set(nums + [num * 2 for num in nums]))
        value_to_rank = {value: rank for rank, value in enumerate(sorted_candidates)}

        seg_tree = ST(len(sorted_candidates))
        answer = 0

        # 오른쪽에서 왼쪽으로 순회하며,
        # 현재 num보다 작은 (오른쪽 원소의 2배 값) 개수를 누적
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            current_rank = value_to_rank[num]

            if current_rank > 0:
                answer += seg_tree.query(
                    0,
                    len(sorted_candidates) - 1,
                    1,
                    0,
                    current_rank - 1,
                )

            # 현재 num에 대해 이후 왼쪽 원소가 비교할 수 있도록 2*num 위치 갱신
            seg_tree.update(
                0,
                len(sorted_candidates) - 1,
                1,
                value_to_rank[num * 2],
            )

        return answer
