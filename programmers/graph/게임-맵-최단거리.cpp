#include<vector>
#include<queue>
#include<iostream> 
#include<tuple>

using namespace std;

int solution(vector<vector<int> > maps) {
    int m = maps.size(), n = maps[0].size();
    int INF = 1e9;
    
    auto onboard = [&](int x, int y) {
        return 0 <= x && x < m && 0 <= y && y < n;
    };

    queue<tuple<int, int, int>> q;
    q.push({0, 0, 0});
    
    vector<vector<int>> dist(m, vector<int>(n, INF));
    // x, y, dist
    
    while (!q.empty()) {
        auto [x, y, d] = q.front();
        q.pop();
        
        dist[x][y] = d;
        if (x == m - 1 && y == n - 1)
            return d + 1;
        
        int dirs[] = {1, 0, -1, 0, 1};
        for (int i = 0; i < 4; i++) {
            int nx = x + dirs[i], ny = y + dirs[i + 1];
            int nd = d + 1;
            
            if (!onboard(nx, ny))
                continue;
            if (maps[nx][ny] == 0)
                continue;
            
            if (dist[nx][ny] > nd) {
                dist[nx][ny] = nd;
                q.push({nx, ny, nd});
            }
        }
    }
    
    return -1;
}
