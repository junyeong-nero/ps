#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
#include <map>
#include <functional>

using namespace std;

class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        map<int, vector<pair<int, int>>> graph;
        for (auto& road : roads) {
            int a = road[0];
            int b = road[1];
            int w = road[2];

            graph[a].push_back({b, w});
            graph[b].push_back({a, w});
        }

        const int INF = 1e9;
        vector<int> dist(n + 1, INF);

        priority_queue<pair<int, int>,
                       vector<pair<int, int>>,
                       greater<pair<int, int>>> pq;

        dist[1] = INF;
        pq.push({INF, 1}); // {현재까지 경로의 최소 edge 값, 노드}

        while (!pq.empty()) {
            auto [cur_dist, cur] = pq.top();
            pq.pop();

            if (cur_dist < dist[cur])
                continue;

            for (auto& [next, weight] : graph[cur]) {
                int new_dist = min(cur_dist, weight);
                if (dist[next] > new_dist) {
                    dist[next] = new_dist;
                    pq.push({new_dist, next});
                }
            }
        }

        return dist[n];
    }
};
