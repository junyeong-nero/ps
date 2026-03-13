class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:

        # find number of non-empty beautiful substrings
        # O(n log n)

        # counter[0] = vowels,
        # counter[1] = consonants
        counter = [0, 0]

        # d[a][b] # of remainder of vowels (a) and consonants (b)
        d = defaultdict(dict)
        d[0][(0, 0)] = 1

        res = 0

        for i, s in enumerate(s):

            index = 0 if s in "aeiou" else 1
            counter[index] += 1

            # need optimizations!!
            diff = counter[0] - counter[1]

            # p * q = counter[0] * counter[1] + x * y - x * counter[1] - y * counter[1]
            #       = a * b + c * d - c * a - b * d

            for x, y in d[diff]:
                p, q = counter[0] - x, counter[1] - y
                if p * q % k == 0:
                    res += d[diff][(x, y)]

            d[diff][(counter[0] % k, counter[1] % k)] = (
                d[diff].get((counter[0] % k, counter[1] % k), 0) + 1
            )

        return res

