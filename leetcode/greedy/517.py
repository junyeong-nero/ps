from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total_dresses = sum(machines)
        
        if total_dresses % n != 0:
            return -1
        
        target_dresses = total_dresses // n
        moves = 0
        dresses_so_far = 0
    
        # prefix sum
        for i in range(n):
            dresses_so_far += machines[i] - target_dresses
            # The maximum value of abs(dresses_so_far) indicates the 
            # maximum number of dresses that needs to be moved in a single move
            moves = max(moves, abs(dresses_so_far), machines[i] - target_dresses)
        
        return moves
