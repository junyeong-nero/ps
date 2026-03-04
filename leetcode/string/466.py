class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        sn2 = len(s2)

        bc = [-1] * sn2
        mc = [-1] * sn2

        block_count = match_count = j_ptr_idx = 0
        a, b = s1, s2
        while bc[j_ptr_idx] == -1:

            bc[j_ptr_idx], mc[j_ptr_idx] = block_count, match_count

            for c in a:
                if c == b[j_ptr_idx]:
                    j_ptr_idx += 1
                    if j_ptr_idx == sn2:
                        j_ptr_idx = 0
                        match_count += 1

            block_count += 1

        blocks = block_count - bc[j_ptr_idx]
        matches = match_count - mc[j_ptr_idx]

        rem_blocks = n1 - block_count
        cycles = rem_blocks // blocks
        match_count += cycles * matches
        block_count += cycles * blocks

        for _ in range(n1 - block_count):
            for c in s1:
                if c == s2[j_ptr_idx]:
                    j_ptr_idx += 1
                    if j_ptr_idx == sn2:
                        j_ptr_idx = 0
                        match_count += 1

        return match_count // n2


# class Solution:
#     def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:

#         t = gcd(n1, n2)
#         n1 //= t
#         n2 //= t

#         str1, str2 = s1 * n1, s2 * n2
#         # str1 = abcabcabcabc
#         # str2 = abab -> abababab (with m = 2)
#         # abcabcabcabc -> abababab

#         def check(src, trg):
#             # src -> trg check

#             if len(src) < len(trg):
#                 return False

#             i = 0
#             for char in src:
#                 if char == trg[i]:
#                     i += 1
#                 if i == len(trg):
#                     return True

#             return False

#         left, right = 1, len(str1) // len(str2) + 1
#         while left < right:
#             mid = (right + left) // 2
#             if check(str1, str2 * mid):
#                 left = mid + 1
#             else:
#                 right = mid

#         # how to handle TLE?
#         # adjust lower bound? or other approach?

#         # s1 * n1 -> s2 * n2 * m
#         # divide n1 and n2 with gcd(n1, n2)


#         return left - 1
