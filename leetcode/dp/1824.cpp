class Solution {
public:
    int minSideJumps(vector<int>& obstacles) {
        int n = obstacles.size() - 1;
        int INF = 1e9;

        vector<vector<int>> dp(4, vector<int>(n + 1, INF));
        dp[1][0] = 1;
        dp[2][0] = 0;
        dp[3][0] = 1;

        for (int point = 1; point <= n; point++) {
            // 이전 위치에서 그대로 전진
            for (int lane = 1; lane <= 3; lane++) {
                if (obstacles[point] == lane) continue;
                dp[lane][point] = dp[lane][point - 1];
            }

            // 현재 위치에서 side jump
            int minVal = INF;
            for (int lane = 1; lane <= 3; lane++) {
                if (obstacles[point] == lane) continue;
                minVal = min(minVal, dp[lane][point]);
            }

            for (int lane = 1; lane <= 3; lane++) {
                if (obstacles[point] == lane) continue;
                dp[lane][point] = min(dp[lane][point], minVal + 1);
            }
        }

        return min({dp[1][n], dp[2][n], dp[3][n]});
    }
};
