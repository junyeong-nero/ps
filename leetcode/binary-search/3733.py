class Solution(object):
    def minimumTime(self, d, r):
        need_a, need_b = d
        rate_a, rate_b = r

        left, right = 0, max(100, (need_a + need_b) * max(rate_a, rate_b))
        lcm = (rate_a * rate_b) // self.gcd(rate_a, rate_b)

        while left <= right:
            mid = (left + right) // 2

            count_a = mid - mid // rate_a
            count_b = mid - mid // rate_b
            common = mid - (mid // rate_a + mid // rate_b - mid // lcm)

            if (
                count_a >= need_a and
                count_b >= need_b and
                count_a + count_b - common >= need_a + need_b
            ):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
