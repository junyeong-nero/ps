#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> data) {
    vector<int> xs, ys;
    
    for (auto& p : data) {
        xs.push_back(p[0]);
        ys.push_back(p[1]);
    }
    
    sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());
    
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());
    
    map<int, int> x_coords, y_coords;
    for (int i = 0; i < (int)xs.size(); i++) x_coords[xs[i]] = i;
    for (int i = 0; i < (int)ys.size(); i++) y_coords[ys[i]] = i;
    
    int xn = x_coords.size();
    int yn = y_coords.size();
    
    vector<pair<int, int>> points;
    vector<vector<int>> grid(xn, vector<int>(yn, 0));
    
    for (auto& p : data) {
        int x = x_coords[p[0]];
        int y = y_coords[p[1]];
        points.push_back({x, y});
        grid[x][y] = 1;
    }
    
    vector<vector<int>> dp(xn + 1, vector<int>(yn + 1, 0));
    
    for (int x = 1; x <= xn; x++) {
        for (int y = 1; y <= yn; y++) {
            dp[x][y] = grid[x - 1][y - 1]
                     + dp[x - 1][y]
                     + dp[x][y - 1]
                     - dp[x - 1][y - 1];
        }
    }
    
    int answer = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int x1 = points[i].first;
            int y1 = points[i].second;
            int x2 = points[j].first;
            int y2 = points[j].second;
            
            int xlo = min(x1, x2);
            int xhi = max(x1, x2);
            int ylo = min(y1, y2);
            int yhi = max(y1, y2);
            
            int cnt = dp[xhi][yhi]
                    - dp[xlo + 1][yhi]
                    - dp[xhi][ylo + 1]
                    + dp[xlo + 1][ylo + 1];
            
            if (cnt == 0 && (xhi - xlo) * (yhi - ylo) > 0) {
                answer++;
            }
        }
    }
    
    return answer;
}
