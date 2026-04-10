#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, int m, vector<vector<int>> edge_list, int k, vector<int> gps_log) {
    const int INF = 1e9;
    
    vector<vector<int>> graph(n + 1);
    
    for (auto &edge : edge_list) {
        int u = edge[0];
        int v = edge[1];
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    // 제자리에 머무를 수도 있음
    for (int i = 1; i <= n; i++) {
        graph[i].push_back(i);
    }
    
    vector<vector<int>> dp(k, vector<int>(n + 1, INF));
    
    // 시작점은 gps_log[0]으로 고정
    dp[0][gps_log[0]] = 0;
    
    for (int t = 1; t < k; t++) {
        for (int prev = 1; prev <= n; prev++) {
            if (dp[t - 1][prev] == INF) continue;
            
            for (int next : graph[prev]) {
                int cost = (next == gps_log[t]) ? 0 : 1;
                dp[t][next] = min(dp[t][next], dp[t - 1][prev] + cost);
            }
        }
    }
    
    // 마지막 시점의 실제 위치도 gps_log[k-1]여야 함
    int answer = dp[k - 1][gps_log[k - 1]];
    
    return answer == INF ? -1 : answer;
}
