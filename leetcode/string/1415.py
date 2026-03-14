class Solution:
    def __init__(self):
        self.count = 0

    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (2 ** (n - 1))
        if k > total:
            return ""
        return self._dfs(n, k, "")

    def _dfs(self, n: int, k: int, current: str) -> str:
        if len(current) == n:
            self.count += 1
            return current if self.count == k else ""

        for ch in "abc":
            if current and current[-1] == ch:
                continue
            result = self._dfs(n, k, current + ch)
            if result:
                return result
        return ""
