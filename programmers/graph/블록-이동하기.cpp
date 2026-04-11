#include <string>
#include <vector>
#include <queue>
#include <set>
#include <iostream>

using namespace std;

int M, N;
int INF = 1e9;

bool check(pair<int,int> pos, vector<vector<int>>& board) {
    auto [x, y] = pos;
    if (x < 0 || x >= M || y < 0 || y >= N)
        return false;
    return board[x][y] == 0;
}

int dirs[] = {1, 0, -1, 0, 1};

int bfs(vector<vector<int>>& board) {
    
    using T = pair<int,int>;
    set<pair<T,T>> visited;
    
    queue<pair<T,T>> q;
    q.push({{0, 0}, {0, 1}});
    
    int res = INF;
    int dist = 0;
    
    while (!q.empty()) {
        
        int size = (int)q.size();
        for (int z = 0; z < size; z++) {
            
            auto [pos1, pos2] = q.front(); q.pop();
            auto [x1, y1] = pos1;
            auto [x2, y2] = pos2;
            
            if (visited.count({pos1, pos2}) || visited.count({pos2, pos1}))
                continue;
            
            visited.insert({pos1, pos2});

            if (x1 == M - 1 && y1 == N - 1)
                return dist;
            if (x2 == M - 1 && y2 == N - 1)
                return dist;

            cout << x1 << ", " << y1 << " - " << x2 << ", " << y2 << endl;

            // rotate
            if (x1 == x2) {
                // horizontal
                
                // y1 기준
                if (check({x2 + 1, y2}, board) && check({x1 + 1, y1}, board)) {
                    q.push({{x1, y1}, {x1 + 1, y1}});
                    q.push({{x2 + 1, y2}, {x2, y2}});
                }                  
                if (check({x2 - 1, y2}, board) && check({x1 - 1, y1}, board)) {
                    q.push({{x2 - 1, y2}, {x2, y2}});
                    q.push({{x1, y1}, {x1 - 1, y1}});
                }
            }
                           
            if (y1 == y2) {
                if (check({x2, y2 + 1}, board) && check({x1, y1 + 1}, board)) {
                    q.push({{x1, y1}, {x1, y1 + 1}});
                    q.push({{x2, y2 + 1}, {x2, y2}});
                }
                if (check({x2, y2 - 1}, board) && check({x1, y1 - 1}, board)) {
                    q.push({{x1, y1}, {x1, y1 - 1}});
                    q.push({{x2, y2 - 1}, {x2, y2}});
                }
            }

            // move
            for (int i = 0; i < 4; i++) {
                int dx = dirs[i];
                int dy = dirs[i + 1];

                int nx1 = x1 + dx;
                int ny1 = y1 + dy;
                int nx2 = x2 + dx;
                int ny2 = y2 + dy;

                pair<int,int> new_pos1 = {nx1, ny1};
                pair<int,int> new_pos2 = {nx2, ny2};

                if (visited.count({new_pos1, new_pos2}) || visited.count({new_pos2, new_pos1}))
                    continue;

                if (check(new_pos1, board) && check(new_pos2, board)) {
                    q.push({new_pos1, new_pos2});
                }
            }
        }
        
        dist++;
        
    }
    return -1;
}

int solution(vector<vector<int>> board) {
    
    M = board.size();
    N = board[0].size();
    
    int answer = bfs(board);
    return answer;
}
