@cache
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        for num in range(left, right + 1):
            count = bin(num).count("1")
            # print(num, count)
            if is_prime(count):
                res += 1
        return res 
