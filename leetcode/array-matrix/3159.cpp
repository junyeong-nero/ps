class Solution {
public:
    vector<int> occurrencesOfElement(vector<int>& nums, vector<int>& queries, int x) {
        
        vector<int> pos;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == x) {
                pos.push_back(i);
            }
        }

        vector<int> res;
        for (auto query : queries) {
            int index = query - 1;
            if (index >= pos.size())
                res.push_back(-1);
            else
                res.push_back(pos[index]);
        }
        return res;
    }
};
