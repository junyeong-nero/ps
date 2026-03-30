class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        n, m = len(s), len(pattern)

        def z_function(text: str):
            z = [0] * len(text)
            l = r = 0

            for i in range(1, len(text)):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])

                while i + z[i] < len(text) and text[z[i]] == text[i + z[i]]:
                    z[i] += 1

                if i + z[i] - 1 > r:
                    l = i
                    r = i + z[i] - 1

            return z

        z1 = z_function(pattern + s)
        z2 = z_function(pattern[::-1] + s[::-1])

        for i in range(n - m + 1):
            if z1[m + i] + 1 + z2[n - i] >= m:
                return i

        return -1
