class Solution {
public:
    vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int k) {
        vector<int> res(k, 0);
        map<int, set<int>> uam;

        for (auto log : logs) {
            int ID = log[0];
            int time = log[1];
            uam[ID].insert(time);
        }

        for (auto& [key, value] : uam) {
            res[value.size() - 1]++;
        }

        return res;
    }
};
