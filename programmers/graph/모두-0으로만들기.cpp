#include <string>
#include <vector>
#include <iostream>
#include <unordered_map> 
#include <queue>
#include <cstdlib>

using namespace std;

long long solution(vector<int> nodes, vector<vector<int>> edges) {
    int n = nodes.size();

    long long total = 0;
    vector<long long> weight(nodes.begin(), nodes.end());

    for (long long x : weight)
        total += x;

    if (total != 0)
        return -1;

    vector<vector<int>> graph(n);
    vector<int> degree(n, 0);

    for (auto& edge : edges) {
        int u = edge[0], v = edge[1];
        graph[u].push_back(v);
        graph[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }

    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (degree[i] == 1) {
            q.push(i);
        }
    }

    long long res = 0;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        res += llabs(weight[cur]);

        for (int next : graph[cur]) {
            if (degree[next] == 0) continue;

            weight[next] += weight[cur];
            degree[next]--;

            if (degree[next] == 1)
                q.push(next);

            break;
        }

        degree[cur] = 0;
    }

    return res;
}
