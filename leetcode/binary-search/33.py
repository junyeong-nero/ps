class Solution:
    def search(self, arr, target):
        return self.search_in_rotated(arr, target, 0, len(arr) - 1)

    def search_in_rotated(self, arr, target, start, end):
        if arr[start] == target:
            return start

        if arr[end] == target:
            return end

        if start == end:
            return -1

        mid = (start + end) // 2

        result = self.search_in_rotated(arr, target, start, mid)
        result2 = self.search_in_rotated(arr, target, mid + 1, end)

        if result != -1:
            return result
        else:
            return result2
