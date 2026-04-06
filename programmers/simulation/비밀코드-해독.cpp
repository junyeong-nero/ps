#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int compare(vector<int> src, vector<int> trg) { 
    set<int> a(src.begin(), src.end());
    set<int> b(trg.begin(), trg.end());
    set<int> res;
    set_intersection(
        a.begin(), a.end(),
        b.begin(), b.end(),
        inserter(res, res.begin())
    );
    
    return (int)res.size();
}


bool check(vector<int> src, vector<vector<int>>& q, vector<int>& ans) {
    
    int m = q.size();
    for (int i = 0; i < m; i++) {
        if (compare(src, q[i]) != ans[i])
            return false;
    }
    
    return true;
}



int solution(int n, vector<vector<int>> q, vector<int> ans) {
    
    // 30^5 = 3^5 * 100000
    int res = 0;
    
    for (int a = 1; a <= n; a++) {
        for (int b = a + 1; b <= n; b++) {
            for (int c = b + 1; c <= n; c++) {
                for (int d = c + 1; d <= n; d++) {
                    for (int e = d + 1; e <= n; e++) {
                        bool temp  = check({a, b, c, d, e}, q, ans);
                        if (temp) res++;
                    }
                }
            }
        }
    }
    
    return res;
}
