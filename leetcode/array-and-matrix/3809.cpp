#include <algorithm>

class Solution {
public:
    vector<int> bestTower(vector<vector<int>>& towers, vector<int>& center, int radius) {

        int INF = 1e9;
        int cx = center[0], cy = center[1];

        pair<int, int> res = {INF, INF};
        int height = -1;

        for (int i = 0; i < towers.size(); i++) {
            int tx = towers[i][0];
            int ty = towers[i][1];
            int h  = towers[i][2];
            if (abs(tx - cx) + abs(ty - cy) > radius)
                continue;
            
            cout << tx << ", " << ty << ", " << h << "\n";
            if (h > height) {
                res = {tx, ty};
                height = h;
            } else if (h == height) {
                res = min(res, {tx, ty});
            }
        }

        if (res.first != INF && res.second != INF)
            return {res.first, res.second};

        return {-1, -1};
    }
};
