class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(elem) for elem in "".join([str(num) for num in nums])]
        
