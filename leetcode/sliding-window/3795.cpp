class Solution {
public:
    int minLength(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        int n = nums.size();
        int res = INT_MAX;

        int sumDistinct = 0;
        int i = 0;

        for (int j = 0; j < n; j++) {
            if (cnt[nums[j]] == 0) {
                sumDistinct += nums[j];
            }
            cnt[nums[j]]++;

            while (sumDistinct >= k) {
                res = min(res, j - i + 1);

                cnt[nums[i]]--;
                if (cnt[nums[i]] == 0) {
                    sumDistinct -= nums[i];
                }
                i++;
            }
        }

        return res == INT_MAX ? -1 : res;
    }
};
