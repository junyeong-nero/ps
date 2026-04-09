#include <vector>

using namespace std;

int MOD = 20170805;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int m, int n, vector<vector<int>> city_map) {
    
    // dir
    // 0 : down
    // 1 : right
    
    // dp[x][y][dir]
    int INF = 1e9;
    
    vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(2, 0)));
    dp[0][0][0] = 1;
    dp[0][0][1] = 1;

    for (int x = 0; x < m; x++) {
        for (int y = 0; y < n; y++) {
            if (city_map[x][y] == 0) {
                if (x - 1 >= 0) {
                    dp[x][y][0] += dp[x - 1][y][0];
                    dp[x][y][1] += dp[x - 1][y][0];
                }
                if (y - 1 >= 0) {
                    dp[x][y][0] += dp[x][y - 1][1];
                    dp[x][y][1] += dp[x][y - 1][1];
                }
            }
            if (city_map[x][y] == 2) {
                if (x - 1 >= 0) dp[x][y][0] += dp[x - 1][y][0];
                if (y - 1 >= 0) dp[x][y][1] += dp[x][y - 1][1];
            }
            dp[x][y][0] %= MOD;
            dp[x][y][1] %= MOD;
        }
    }
    
    int answer = dp[m - 1][n - 1][0] + dp[m - 1][n - 1][1];
    return answer / 2;
}
