#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    const int MOD = 1000000007;
    
    set<pair<int, int>> puddle;
    for (int i = 0; i < puddles.size(); i++) {
        puddle.insert({puddles[i][1], puddles[i][0]}); // (y, x)
    }
    
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    dp[1][1] = 1;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (i == 1 && j == 1) continue;
            if (puddle.find({i, j}) != puddle.end()) continue;
            
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD;
        }
    }
    
    return dp[n][m];
}
