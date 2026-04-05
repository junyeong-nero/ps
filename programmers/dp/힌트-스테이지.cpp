#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int dfs(int n, int level, int total_cost, vector<vector<int>>& cost, vector<vector<int>>& hint,
        vector<int>& counter) {
    int idx = min(n - 1, counter[level]);
    int temp = total_cost + cost[level][idx];

    if (level == n - 1) return temp;

    int res = 1e9;
    res = min(res, dfs(n, level + 1, temp, cost, hint, counter));

    for (int i = 1; i < (int)hint[level].size(); i++) counter[hint[level][i] - 1]++;

    res = min(res, dfs(n, level + 1, temp + hint[level][0], cost, hint, counter));

    for (int i = 1; i < (int)hint[level].size(); i++) counter[hint[level][i] - 1]--;

    return res;
}

int solution(vector<vector<int>> cost, vector<vector<int>> hint) {
    int n = (int)cost.size();
    vector<int> counter(n, 0);
    return dfs(n, 0, 0, cost, hint, counter);
}