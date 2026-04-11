class Solution {
public:
    int maxScore(int n, int k, vector<vector<int>>& stayScore, vector<vector<int>>& travelScore) {
        // dp style solution 
        // dp[i][city] : maximum points at i-th day, city
        // 4 + 4

        vector<vector<int>> dp(k + 1, vector<int>(n, 0));

        for (int day = 1; day <= k; day++) {
            for (int city = 0; city < n; city++) {

                // stay same city
                dp[day][city] = max(dp[day][city], stayScore[day - 1][city] + dp[day - 1][city]);

                // move from other city
                for (int other_city = 0; other_city < n; other_city++) {
                    if (city == other_city) continue;
                    dp[day][city] = max(dp[day][city], travelScore[other_city][city] + dp[day - 1][other_city]);
                }
            }
        }

        int res = 0;
        for (int i = 0; i < n; i++)
            res = max(res, dp[k][i]);

        return res;
    }
};
