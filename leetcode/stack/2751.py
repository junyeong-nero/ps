from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        arr = sorted(zip(positions, healths, directions))
        for pos, hp, direction in arr:
            if direction == "R":
                stack.append([pos, hp, direction])

            if direction == "L":
                can_push = True

                while stack and stack[-1][2] == "R":
                    if stack[-1][1] < hp:
                        stack.pop()
                        hp -= 1
                    elif stack[-1][1] == hp:
                        stack.pop()
                        can_push = False
                        break
                    elif stack[-1][1] > hp:
                        stack[-1][1] -= 1
                        can_push = False
                        break
                
                if can_push:
                    stack.append([pos, hp, direction])

        d = dict()
        for pos, hp, direction in stack:
            d[pos] = hp

        res = [d[pos] for pos in positions if pos in d]
        return res
