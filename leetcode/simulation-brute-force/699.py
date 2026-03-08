class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # 처음에 들어오는 left rㅏ 기존 boundary 안에 있는 경우 -> 그 높이기준으로 더해주면 됨.
        # 1, 2 => [(1, 3):2]
        # 2, 3 => 2가 (1, 3 바운더리 안에 있으므로) => [(1, 2): 2, (2, 5): 5]

        # 진짜 segtree -> 아님.

        d = []
        def overlap(x, y):
            p, q = max(x[0], y[0]), min(x[1], y[1])
            return p < q
        
        def func(left, size):
            temp = 0
            for x in d:
                if overlap(x, (left, left + size)):
                    temp = max(temp, x[2])
            
            d.append((left, left + size, size + temp))
            return size + temp

        res = []
        curr = 0
        for left, size in positions:
            curr = max(curr, func(left, size))
            res.append(curr)
        
        return res

                
            

