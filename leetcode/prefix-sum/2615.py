# class Solution:
#     def distance(self, nums: List[int]) -> List[int]:

#         # arr[i] = sum(|i - j| for nums[i] == nums[j])
#         n = len(nums)

#         d = defaultdict(list)
#         for idx, num in enumerate(nums):
#             d[num].append(idx)

#         print(d)

#         arr = []
#         for idx, num in enumerate(nums):
#             i = bisect_left(d[num], idx)
#             print(idx, i)

#             temp = sum(d[num])
#             temp += (i) * idx
#             temp -= (len(d[num]) - i) * idx

#             arr.append(temp)


#         return arr

#         return []


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num_indices = dict()
        occ = dict()
        for i, num in enumerate(nums):
            if num not in num_indices:
                num_indices[num] = i
                occ[num] = 1
            else:
                num_indices[num] = num_indices[num] + i
                occ[num] = occ[num] + 1

                
        arr = [0] * len(nums)
        n = len(nums)
        for i in range(n):
            arr[i] = num_indices[nums[i]] - occ[nums[i]] * i
            num_indices[nums[i]] = num_indices[nums[i]] - 2 * i
            occ[nums[i]] = occ[nums[i]] - 2

        return arr

