class Solution {
public:
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        
        // n = 10^3
        // solve within O(n^2)
        
        int MOD = 1e9 + 7;

        // O(n^2)
        for (auto query : queries) {
            int l = query[0];
            int r = query[1];
            int k = query[2];
            int v = query[3];

            for (int x = l; x <= r; x += k) {
                nums[x] = ((long)nums[x] * v) % MOD;
            }
        }

        int res = 0;
        for (auto num : nums) {
            res ^= num;
        }
        return res;
    }
};
