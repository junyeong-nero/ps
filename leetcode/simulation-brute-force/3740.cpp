class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        
        int n = nums.size();
        int res = 1e9;

        // O(n^3)
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] == nums[j] && nums[j] == nums[k]) {
                        res = min(res, abs(i - j) + abs(j - k) + abs(k - i));
                    }   
                }
            }
        }

        if (res == 1e9)
            return -1;
            
        return res;
    }
};
