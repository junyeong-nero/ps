#include <string>
#include <vector>

using namespace std;

int INF = 1e9;
int X[] = {
    1, // 0
    0, 1, 2,
    0, 1, 2,
    0, 1, 2,
};

int Y[] = {
    3, // 0
    0, 0, 0,
    1, 1, 1,
    2, 2, 2,
};

int cost(int a, int b) {
    int dx = abs(X[a] - X[b]);
    int dy = abs(Y[a] - Y[b]);
    if (dx == 0 && dy == 0)
        return 1;
    return min(dx, dy) * 3 + (max(dx, dy) - min(dx, dy)) * 2;
}

int solution(string numbers) {
    
    vector<vector<int>> dp(10, vector<int>(10, INF));
    dp[4][6] = 0;
    // dp[left][right] -> minimum cost;
    
    for (int i = 0; i < numbers.size(); i++) {
        
        int cur = numbers[i] - '0';
        vector<vector<int>> new_dp(10, vector<int>(10, INF));
        
        for (int left = 0; left < 10; left++) {
            for (int right = 0; right < 10; right++) {    
                if (cur == left) {
                    new_dp[cur][right] = min(new_dp[cur][right], cost(left, cur) + dp[left][right]);
                } else if (cur == right) {
                    new_dp[left][cur] = min(new_dp[left][cur], cost(right, cur) + dp[left][right]);   
                } else {
                    new_dp[cur][right] = min(new_dp[cur][right], cost(left, cur) + dp[left][right]);
                    new_dp[left][cur] = min(new_dp[left][cur], cost(right, cur) + dp[left][right]);   

                }
            }
        }
        dp = new_dp;
    }
    
    int res = INF;
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 10; j++)
            res = min(res, dp[i][j]);
    
    return res;
}
