#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
int INF = 1e9;

int solve(string t, int index, map<char, vector<string>>& prefix) {

    if (index == t.size())
        return 0;
    
    int res = INF;
    for (string s : prefix[t[index]]) {
        int n = s.size();
        string temp = t.substr(index, n);
        if (temp.size() == n && s == temp) {
            res = min(res, 1 + solve(t, index + n, prefix));
        }
    }
    return res;
}


int solution(vector<string> strs, string t) {
    
    // map<char, vector<string>> prefix;
    // for (string s : strs) {
    //     prefix[s[0]].push_back(s);
    // }
    
    map<char, vector<string>> suffix;
    for (string s : strs) {
        suffix[s.back()].push_back(s);
    }
    
    // dp[i] : i 까지 minimum count.
    // dp[0] = 0
    // dp[i] = dp[i - m] + 1 if t[i:i + m] == s
    int n = t.size();
    vector<int> dp(n + 1, INF);
    dp[0] = 0;
    
    for (int i = 1; i <= n; i++) {
        
        char c = t[i - 1];
        for (string s : suffix[c]) {
            
            int m = s.size();
            if (i - m >= 0) {
                string temp = t.substr(i - m, m);           
                if (s == temp)
                    dp[i] = min(dp[i], dp[i - m] + 1);
            }
        }
    }
    
    int res = dp[n];
    return res == INF ? -1 : res;
}
