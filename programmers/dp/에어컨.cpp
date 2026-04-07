#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int T_outside, T1, T2, A, B; 
int INF = 1e9;
int dp[1005][55];

int dfs(int index, int t, vector<int>& onboard) {
    if (dp[index][t + 10] != -1)
        return dp[index][t + 10];
    if (t < -10 || t > 40) 
        return INF;
    if (index == onboard.size())
        return 0;
    if (onboard[index] == 1) {
        if (t < T1 || t > T2) {
            return INF;
        }
    }
    
    int res = INF;
    int dt = 0;
    if (t < T_outside)
        dt = 1;
    if (t > T_outside)
        dt = -1;
    
    res = min(res, dfs(index + 1, t + dt, onboard));
    res = min(res, B + dfs(index + 1, t, onboard));   
    res = min(res, A + dfs(index + 1, t + 1, onboard)); 
    res = min(res, A + dfs(index + 1, t - 1, onboard));
    
    dp[index][t + 10] = res;
    return res;
}


int solution(int temperature, int t1, int t2, int a, int b, vector<int> onboard) {
    
    T_outside = temperature;
    T1 = t1, T2 = t2, A = a, B = b;
    
    for (int i = 0; i < 1005; i++)
        for (int j = 0; j < 55; j++)
            dp[i][j] = -1;
    
    int answer = dfs(0, temperature, onboard);
    return answer;
}
