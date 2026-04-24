class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False

        nums.sort(reverse=True)
        bound = total // k
        # print(bound)

        arr = [0] * k

        def dfs(index):

            if index == n:
                return True
            
            for i in range(k):
                if arr[i] + nums[index] > bound: continue

                arr[i] += nums[index]
                if dfs(index + 1):
                    return True
                arr[i] -= nums[index]
                if arr[i] == 0:
                    break

            return False

        res = dfs(0)
        return res


