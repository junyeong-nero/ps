#include <iostream>
using namespace std;

class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        
        int n = nums.size();
        map<int, vector<int>> d;
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            d[num].push_back(i);
        }

        int res = 1e9;
        for (auto [key, arr] : d) {

            if (arr.size() < 3)
                continue;

            int m = arr.size();
            for (int p = 0; p < m - 2; p++) {
                int i = arr[p];
                int j = arr[p + 1];
                int k = arr[p + 2];
                res = min(res, (j - i) + (k - j) + (k - i));
            }
        }

        return res == 1e9 ? -1 : res;
    }
};
