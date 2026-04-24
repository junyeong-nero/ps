class Solution:
    def longestDecomposition(self, text: str) -> int:
        # split with k substrings
        # subtext(i)

        # left, right
        # left 이동, text[left] == text[right] 인 경우에
        #

        n = len(text)

        @cache
        def dfs(left, right):

            if left > right:
                return 0

            for i in range(left, n):
                size = i - left + 1
                if (
                    text[i] == text[right]
                    and text[left : left + size] == text[right + 1 - size : right + 1]
                ):
                    return (1 if i >= right else 2) + dfs(left + size, right - size)

            return 1

        return dfs(0, n - 1)

