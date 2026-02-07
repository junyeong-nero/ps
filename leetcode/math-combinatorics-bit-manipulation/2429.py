class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a = bin(num1).count('1')
        b = bin(num2).count('1')
        
        if a == b:
            return num1
        
        res = num1
        if a > b:
            # 1의 개수를 줄여야 함: 가장 낮은 자리의 1부터 제거
            diff = a - b
            for i in range(32):
                if diff <= 0: break
                if (res >> i) & 1:
                    res &= ~(1 << i)
                    diff -= 1
        else:
            # 1의 개수를 늘려야 함: 가장 낮은 자리의 0부터 1로 변경
            diff = b - a
            for i in range(32):
                if diff <= 0: break
                if not ((res >> i) & 1):
                    res |= (1 << i)
                    diff -= 1
                    
        return res