#include <algorithm>

class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        
        int dir = 0;
        int x = 0, y = 0;

        int dx[4] = {0, 1, 0, -1};
        int dy[4] = {1, 0, -1, 0};

        // -1 => d++;
        // -2 => d--;

        int answer = 0;

        set<pair<int,int>> obs;
        for (auto obstacle : obstacles) {
            obs.insert({obstacle[0], obstacle[1]});
        }

        for (auto cmd : commands) {
            if (cmd == -2)
                dir = (dir - 1 + 4) % 4; 
            if (cmd == -1)
                dir = (dir + 1 + 4) % 4; 
            if (cmd > 0) {
                for (int i = 0; i < cmd; i++) {
                    x += dx[dir];
                    y += dy[dir];

                    if (obs.count({x, y})) {
                        x -= dx[dir];
                        y -= dy[dir];    
                        break;
                    }
                    
                    answer = max(answer, x * x + y * y);
                }

                // cout << x << ", " << y << "\n";
            }
        }

        return answer;
    }
};
