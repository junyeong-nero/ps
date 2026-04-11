class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        
        // 2^100 = 10^10
        // DFS 로는 절대 안됨.
        
        int n = costs.size();
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> city1;
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> city2;

        // 일단 최소경우만 뽑는 경우.
        // city1 > city2 인 경우 -> city1 으로 뽑힌 사람들 중에서 diff 가 가장 작은 녀석들을 city2 로 가도록 해야함.

        for (int i = 0; i < n; i++) {
            if (costs[i][0] < costs[i][1])
                city1.push({costs[i][1] - costs[i][0], i});
            else
                city2.push({costs[i][0] - costs[i][1], i});
        }

        while (city1.size() > city2.size()) {
            auto [diff, idx] = city1.top(); city1.pop();
            city2.push({diff, idx});
        }

        while (city2.size() > city1.size()) {
            auto [diff, idx] = city2.top(); city2.pop();
            city1.push({diff, idx});
        }

        int res = 0;

        while (!city1.empty()) {
            auto [diff, idx] = city1.top(); city1.pop();
            res += costs[idx][0];
            // cout << costs[idx][0] << endl;
        }
        while (!city2.empty()) {
            auto [diff, idx] = city2.top(); city2.pop();
            res += costs[idx][1];
            // cout << costs[idx][1] << endl;
        }

        return res;
    } 
};
