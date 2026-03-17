### Binary Search : TLE

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        # maximize XOR among all strong pairs
        # position does not matter -> counter based approach
        # n = 5 * 10^4
        # O(n log n) time complexity
        # if x == y: it should be ignored.

        nums = sorted(set(nums))
        n = len(nums)
        res = 0

        for y in range(n):

            # y is fixed, then find abs(nums[x] - nums[y]) - min(nums[x], nums[y]) <= 0
            # it is equivalent to (nums[y] - nums[x]) - nums[x] <= 0
            #                      nums[y] / 2 <= nums[x] < nums[y]

            start = bisect_left(nums, nums[y] / 2)
            for x in range(start, y):
                # print(nums[x], nums[y], nums[x] ^ nums[y])
                res = max(res, nums[x] ^ nums[y])

        return res


from typing import List


class TreeNode:
    def __init__(self):
        # children[0] = bit가 0인 자식
        # children[1] = bit가 1인 자식
        self.children = [None, None]
        
        # 이 노드를 지나는 숫자의 개수
        # 삭제(remove) 연산을 위해 필요
        self.cnt = 0


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # 숫자를 정렬하면 strong pair 조건을
        # y <= 2*x 형태로 다루기 쉬워진다.
        nums.sort()
        
        root = TreeNode()
        
        # 문제의 nums[i] 범위는 보통 2^20 이하이므로
        # 20비트 ~ 0비트까지 보면 충분하다.
        # 안전하게 20부터 사용
        HIGH_BIT = 20
        
        def insert(num: int) -> None:
            """숫자를 Trie에 삽입"""
            node = root
            node.cnt += 1
            
            for bit in range(HIGH_BIT, -1, -1):
                b = (num >> bit) & 1
                
                if node.children[b] is None:
                    node.children[b] = TreeNode()
                
                node = node.children[b]
                node.cnt += 1
        
        def remove(num: int) -> None:
            """숫자를 Trie에서 제거"""
            node = root
            node.cnt -= 1
            
            for bit in range(HIGH_BIT, -1, -1):
                b = (num >> bit) & 1
                nxt = node.children[b]
                nxt.cnt -= 1
                node = nxt
        
        def get_max_xor(num: int) -> int:
            """
            현재 Trie 안에 있는 숫자들 중
            num과 XOR 값이 최대가 되는 값을 찾는다.
            """
            node = root
            xor_val = 0
            
            for bit in range(HIGH_BIT, -1, -1):
                b = (num >> bit) & 1
                
                # XOR을 키우려면 현재 비트와 반대 비트로 가는 게 좋다.
                want = 1 - b
                
                if node.children[want] is not None and node.children[want].cnt > 0:
                    # 반대 비트가 존재하면 그쪽으로 이동
                    xor_val |= (1 << bit)
                    node = node.children[want]
                else:
                    # 없으면 같은 비트 쪽으로 이동
                    node = node.children[b]
            
            return xor_val
        
        ans = 0
        left = 0
        
        for right in range(len(nums)):
            y = nums[right]
            
            # 현재 y와 strong pair가 될 수 없는 작은 값들은 제거
            # 정렬되어 있고 x <= y 이므로
            # strong pair 조건은 y <= 2*x 와 같다.
            while left <= right and y > 2 * nums[left]:
                remove(nums[left])
                left += 1
            
            # 현재 숫자 y를 Trie에 삽입
            # 자기 자신과도 pair 가능하므로 먼저 넣어도 된다.
            insert(y)
            
            # 현재 윈도우 안의 값들과 y의 최대 XOR 계산
            ans = max(ans, get_max_xor(y))
        
        return ans
