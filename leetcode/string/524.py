from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        n = len(s)
        # next_pos[i][k] = i 이상에서 chr(ord('a')+k)가 처음 나오는 인덱스, 없으면 -1
        next_pos = [[-1] * 26 for _ in range(n + 2)]

        # i = n 위치(문자열 끝)에서는 전부 -1
        for k in range(26):
            next_pos[n][k] = -1

        # 뒤에서 앞으로 채우기
        for i in range(n - 1, -1, -1):
            next_pos[i] = next_pos[i + 1].copy()
            next_pos[i][ord(s[i]) - 97] = i

        def is_subseq(word: str) -> bool:
            idx = 0  # s에서 현재 탐색 시작 위치
            for ch in word:
                k = ord(ch) - 97
                if idx > n:
                    return False
                j = next_pos[idx][k]
                if j == -1:
                    return False
                idx = j + 1
            return True

        best = ""
        for w in dictionary:
            # 길이 우선, 길이가 같으면 사전순(lexicographically smallest)
            if (len(w) > len(best)) or (len(w) == len(best) and w < best):
                if is_subseq(w):
                    best = w

        return best

# class Solution:
#     def findLongestWord(self, s: str, dictionary: List[str]) -> str:
#         # trie
#         n = len(s)
#         trie = dict()

#         def insert(word):
#             curr = trie
#             for char in word:
#                 if char not in curr:
#                     curr[char] = dict()
#                 curr = curr[char]

#             curr["#"] = word

#         for word in dictionary:
#             insert(word)

#         # print(trie)
#         hist = []

#         @cache
#         def dfs(cur, index):
#             if "#" in cur:
#                 nonlocal hist
#                 if hist and len(hist[0]) < len(cur["#"]):
#                     hist.clear()
#                 if not hist or len(hist[0]) <= len(cur["#"]):
#                     hist.append(cur["#"])

#             if index == n:
#                 return

#             dfs(cur, index + 1)
#             if s[index] in cur:
#                 dfs(cur[s[index]], index + 1)

#         dfs(trie, 0)
#         return min(hist) if hist else ""
