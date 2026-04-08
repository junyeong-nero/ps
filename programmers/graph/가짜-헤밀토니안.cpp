#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

unordered_map<long long, int> dfsMemo;
unordered_map<long long, int> funcMemo;

long long makeKey(int cur, int prev) {
    return (static_cast<long long>(cur) << 32) | static_cast<unsigned int>(prev + 1);
}

int dfs(int cur, int prev, unordered_map<int, vector<int>>& graph) {
    long long key = makeKey(cur, prev);
    if (dfsMemo.find(key) != dfsMemo.end()) return dfsMemo[key];

    int depth = 1;
    for (int node : graph[cur]) {
        if (node == prev) continue;
        depth = max(depth, 1 + dfs(node, cur, graph));
    }

    return dfsMemo[key] = depth;
}

int func(int cur, int prev, unordered_map<int, vector<int>>& graph) {
    long long key = makeKey(cur, prev);
    if (funcMemo.find(key) != funcMemo.end()) return funcMemo[key];

    int res = 1;

    int max1 = 0, max2 = 0; // 자식 방향 dfs depth 중 1등, 2등
    for (int node : graph[cur]) {
        if (node == prev) continue;

        int d = dfs(node, cur, graph);
        if (d > max1) {
            max2 = max1;
            max1 = d;
        } else if (d > max2) {
            max2 = d;
        }
    }

    for (int node : graph[cur]) {
        if (node == prev) continue;

        int d = dfs(node, cur, graph);
        int bestOther = (d == max1 ? max2 : max1);

        res = max(res, 1 + bestOther + func(node, cur, graph));
    }

    return funcMemo[key] = res;
}

int solution(vector<vector<int>> t) {
    int n = t.size() + 1;
    unordered_map<int, vector<int>> graph;

    for (auto& arr : t) {
        int u = arr[0], v = arr[1];
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    dfsMemo.clear();
    funcMemo.clear();

    int res = 0;
    for (int node = 0; node < n; node++) {
        if (graph[node].size() > 1) continue; // leaf만 시작점
        res = max(res, func(node, -1, graph));
    }

    return res;
}
