class Solution {
    public int findMin(int[] nums) {
        return findMinDPS(nums, 0, nums.length - 1);
    }

    public int findMinDPS(int[] nums, int start, int end) {
        if (start == end) return nums[start];
        if (nums[start] < nums[end]) return nums[start];
        int min = (start + end) / 2;
        return Math.min(findMinDPS(nums, start, min), findMinDPS(nums, min + 1, end));
    }
}
