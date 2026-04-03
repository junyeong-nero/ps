#include <cmath>

class Solution {
public:
    int maximumAmount(vector<vector<int>>& coins) {
        // right or down
        int m = coins.size();
        int n = coins[0].size();

        int NEG = -1e9;

        // dp[k][i][j] k = stealing neutralize / (i, j) = position
        vector<vector<vector<int>>> dp(3, vector<vector<int>>(m + 1, vector<int>(n + 1, NEG)));
        dp[0][0][1] = 0;
        dp[1][0][1] = 0;
        dp[2][0][1] = 0;
        dp[0][1][0] = 0;
        dp[1][1][0] = 0;
        dp[2][1][0] = 0;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int diff = coins[i - 1][j - 1];
            
                dp[0][i][j] = max(dp[0][i][j], diff + max(dp[0][i][j - 1], dp[0][i - 1][j]));
                dp[1][i][j] = max(dp[1][i][j], diff + max(dp[1][i][j - 1], dp[1][i - 1][j]));
                dp[2][i][j] = max(dp[2][i][j], diff + max(dp[2][i][j - 1], dp[2][i - 1][j]));
                
                if (diff < 0) {
                    dp[1][i][j] = max(dp[1][i][j], max(dp[0][i][j - 1], dp[0][i - 1][j]));
                    dp[2][i][j] = max(dp[2][i][j], max(dp[1][i][j - 1], dp[1][i - 1][j]));
                }
                
            }
        }

        return max({dp[0][m][n], dp[1][m][n], dp[2][m][n]});
    }
};
