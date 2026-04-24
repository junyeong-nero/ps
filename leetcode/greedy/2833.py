class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        min_pos, max_pos = float("inf"), float("-inf")
        pos = 0
        diff = 0

        for move in moves:
            if move == "L":
                pos -= 1
            if move == "R":
                pos += 1            
            if move == "_":
                diff += 1
        
        return max(abs(pos + diff), abs(pos - diff))
