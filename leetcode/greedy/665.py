class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        # 1 2 3 10 5 6 7
        
        n = len(nums)
        count = 0
        i = 0
        arr = []

        while i < n:
            j = i
            while j + 1 < n and nums[j] <= nums[j + 1]:
                j += 1
            
            arr.append((i, j))
            i = j + 1

        if len(arr) <= 1:
            return True
            
        if len(arr) == 2:
            # 어짜피 하나밖에 없는 경우
            if arr[0][0] == arr[0][1] or arr[1][0] == arr[1][1]:
                return True

            left = arr[0][1]
            if nums[left - 1] <= nums[left + 1]:
                return True

            right = arr[1][0]
            if nums[right - 1] <= nums[right + 1]:
                return True

        return False 

