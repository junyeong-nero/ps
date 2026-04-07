#include <vector>
#include <algorithm>
using namespace std;

int solveLinear(const vector<int>& sticker, int start, int end) {
    int len = end - start + 1;
    if (len == 1) return sticker[start];

    vector<int> dp(len, 0);
    dp[0] = sticker[start];
    dp[1] = max(sticker[start], sticker[start + 1]);

    for (int i = 2; i < len; i++) {
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[start + i]);
    }

    return dp[len - 1];
}

int solution(vector<int> sticker) {
    int n = sticker.size();
    if (n == 1) return sticker[0];

    int case1 = solveLinear(sticker, 0, n - 2); // 첫 번째 포함 가능, 마지막 제외
    int case2 = solveLinear(sticker, 1, n - 1); // 첫 번째 제외, 마지막 포함 가능

    return max(case1, case2);
}

// #include <iostream>
// #include <vector>
// using namespace std;

// int INF = 1e9;
// int n;
// int dp[2][100001];

// int dfs(int index, int used, vector<int>& sticker) {
//     if (index >= n)
//         return 0;
//     if (dp[used][index] != -1)
//         return dp[used][index];
    
//     int res = -INF;
//     res = max(res, dfs(index + 1, used, sticker));
//     if (index == 0) {
//         res = max(res, sticker[index] + dfs(index + 2, 1, sticker));
//     } else if (index < n - 1 || !used) {
//         res = max(res, sticker[index] + dfs(index + 2, used, sticker));
//     }
        
//     dp[used][index] = res;
//     return res;
    
// }

// int solution(vector<int> sticker) {
    
//     n = sticker.size();
//     for (int i = 0; i < 100001; i++) {
//         dp[0][i] = -1;
//         dp[1][i] = -1;
//     }
        
//     int answer = dfs(0, 0, sticker);
//     return answer;
// }
