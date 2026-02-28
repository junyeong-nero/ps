from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(
        self, m: int, n: int, head: Optional[ListNode]
    ) -> List[List[int]]:
        
        board = [[-1] * n for _ in range(m)]
        dirs = [0, 1, 0, -1, 0]
        current_dir = 0

        def get_next(x, y):
            nonlocal current_dir
            nx, ny = x + dirs[current_dir], y + dirs[current_dir + 1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or board[nx][ny] != -1:
                current_dir = (current_dir + 1) % 4
                nx, ny = x + dirs[current_dir], y + dirs[current_dir + 1]

            return nx, ny

        x, y = 0, 0
        curr = head
        while curr:
            board[x][y] = curr.val
            x, y = get_next(x, y)
            curr = curr.next

        return board
