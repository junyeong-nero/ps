#include <string>
#include <vector>
#include <iostream>
#include <deque>

using namespace std;



vector<bool> spread(
        int n, 
        int type,
        vector<vector<int>>& graph, 
        vector<bool> infected
    ) {
    
    deque<int> q;
    for (int i = 0; i < n; i++) {
        if (infected[i])
            q.push_back(i);
    }
    
    while (!q.empty()) {
        int cur = q.front();
        q.pop_front();
        
        infected[cur] = true;
        
        for (int node = 0; node < n; node++) {
            if (graph[cur][node] == type && !infected[node]) {
                q.push_back(node);
            }
        }
    }
    return infected;
}


int dfs(int n, int k, vector<vector<int>>& graph, vector<bool> infected) {
    if (k == 0) {
        int count = 0;
        for (int i = 0; i < n; i++)
            if (infected[i])
                count++;
        return count;
    }
    
    int res = 0;
    res = max(res, dfs(n, k - 1, graph, spread(n, 1, graph, infected)));
    res = max(res, dfs(n, k - 1, graph, spread(n, 2, graph, infected)));
    res = max(res, dfs(n, k - 1, graph, spread(n, 3, graph, infected)));
    
    return res;
}

int solution(int n, int infection, vector<vector<int>> edges, int k) {
    
    // 3**k <= 60000 -> 완전 탐색으로도 충분
    
    vector<vector<int>> graph(n, vector<int>(n, 0));
    for (auto edge : edges) {
        int x = edge[0] - 1;
        int y = edge[1] - 1;
        int type = edge[2];
        
        graph[x][y] = type;
        graph[y][x] = type;
    }
    
    vector<bool> infected(n, false);
    infected[infection - 1] = true;

    int answer = dfs(n, k, graph, infected);
    return answer;
}
