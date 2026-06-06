class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        leftSum = [0]
        rightSum = [sum(nums)]

        for num in nums:
            leftSum.append(leftSum[-1] + num)
            rightSum.append(rightSum[-1] - num)

        rightSum = rightSum[1:]

        res = []
        for i in range(len(nums)):
            res.append(abs(leftSum[i] - rightSum[i]))

        return res
