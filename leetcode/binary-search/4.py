class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)

        # Always binary search on the smaller array.
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        total_len = len1 + len2
        left_partition_size = (total_len + 1) // 2

        low, high = 0, len1

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = left_partition_size - partition1

            left1 = float("-inf")
            right1 = float("inf")
            left2 = float("-inf")
            right2 = float("inf")

            if partition1 < len1:
                right1 = nums1[partition1]
            if partition2 < len2:
                right2 = nums2[partition2]
            if partition1 > 0:
                left1 = nums1[partition1 - 1]
            if partition2 > 0:
                left2 = nums2[partition2 - 1]

            # Correct partition found.
            if left1 <= right2 and left2 <= right1:
                if total_len % 2 == 1:
                    return max(left1, left2)

                return (max(left1, left2) + min(right1, right2)) / 2.0

            # Move search space left.
            if left1 > right2:
                high = partition1 - 1
            # Move search space right.
            else:
                low = partition1 + 1

        return 0
