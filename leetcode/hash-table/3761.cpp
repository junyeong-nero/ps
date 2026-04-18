class Solution {
    
public:

    int get_reverse(int num) {
        string s = to_string(num);
        reverse(s.begin(), s.end());
        return stoi(s);
    }

    int minMirrorPairDistance(vector<int>& nums) {
        int n = nums.size();
        vector<int> nums_r;
        for (auto num : nums) {
            nums_r.push_back(get_reverse(num));
        }

        unordered_map<int,int> d;
        int res = n;

        for (int i = 0; i < n; i++) {
            if (d.count(nums[i]))
                res = min(res, i - d[nums[i]]);
            d[nums_r[i]] = i;
        }

        return res == n ? -1 : res; 
    }
};
