@cache
def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

class Solution:
    def largestPrime(self, n: int) -> int:
        
        res = 0
        cur = 0
        for i in range(2, n + 1):
            if not isprime(i):
                continue
            if cur + i <= n:
                cur += i
                if isprime(cur):
                    res = cur
            else:
                break
        
        return res
