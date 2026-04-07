#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> beginning, vector<vector<int>> target) {
    
    int m = target.size(), n = target[0].size();
    int flip = 0;
    
    for (int i = 0; i < m; i++) {
        if (beginning[i][0] == target[i][0]) 
            continue;
        
        for (int j = 0; j < n; j++) {
            beginning[i][j] ^= 1;
        }
        flip++;
    }
    
    for (int j = 0; j < n; j++) {
        if (beginning[0][j] == target[0][j]) 
            continue;
        for (int i = 0; i < m; i++) {
            beginning[i][j] ^= 1;
        }
        flip++;
    }
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (beginning[i][j] != target[i][j])
                return -1;
        }
    }

    return min(m + n - flip, flip);
}
