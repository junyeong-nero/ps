class Solution:
    def nearestPalindromic(self, n: str) -> str:
        x = int(n)
        m = len(n)

        candidates = set()

        # 경계값 후보
        candidates.add(10 ** (m - 1) - 1)   # 999...9
        candidates.add(10 ** m + 1)         # 1000...0001

        # prefix 추출
        prefix = int(n[: (m + 1) // 2])

        # prefix - 1, prefix, prefix + 1 로 후보 생성
        for p in [prefix - 1, prefix, prefix + 1]:
            s = str(p)
            if m % 2 == 0:
                cand = int(s + s[::-1])
            else:
                cand = int(s + s[-2::-1])
            candidates.add(cand)

        # 자기 자신 제외
        candidates.discard(x)

        # 절대 차이, 동률이면 더 작은 수
        ans = min(candidates, key=lambda y: (abs(y - x), y))
        return str(ans)

# class Solution:
#     def nearestPalindromic(self, n: str) -> str:
#         # closest palindrome, not including itself.
#         # closest -> minimize abs(a, b)

#         # 149 -> 141 / 151
#         # find the maximum palindrome < n
#         # find the minimum palindrome > n

#         # edit start & end points => large diff
#         #   -> edit at middle point first

#         s = n
#         n = len(s)
#         v = int(s)

#         # if len is odd => len // 2
#         # if len is even => modify both n // 2 and n // 2 - 1

#         arr = [int(c) for c in s]
#         for i in range(n):
#             j = n - 1 - i
#             if arr[i] != arr[j]:
#                 arr[j] = arr[i]

#         def convert(arr):
#             temp = "".join([str(c) for c in arr])
#             return temp

#         res = "0"

#         def check(arr):
#             nonlocal res

#             temp = convert(arr)
#             if temp != s and abs(int(res) - v) > abs(int(temp) - v):
#                 res = temp

#         def increment(arr, delta):
#             t = len(arr)
#             half = arr[: t // 2] if t % 2 == 0 else arr[: t // 2 + 1]
#             temp = int(convert(half)) + delta
#             res = (
#                 (str(temp) + str(temp)[::-1])
#                 if t % 2 == 0
#                 else (str(temp) + str(temp)[::-1][1:])
#             )
#             return [int(c) for c in res]

#         check(arr)
#         # print(arr)

#         right = arr[:]
#         while int(convert(right)) >= v:
#             right = increment(right, -1)
#             # print(arr)
#             check(right)

#         left = arr[:]
#         while int(convert(left)) <= v:
#             left = increment(left, 1)
#             # print(arr)
#             check(left)

#         # print(res)
#         return res

