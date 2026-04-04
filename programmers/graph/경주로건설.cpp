#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int dirs[] = {1, 0, -1, 0, 1};
int answer = 1e9;

void dfs(int x, int y, int dir, int cost, vector<vector<int>>& board, vector<vector<vector<int>>>& dist) {
    if (x == N - 1 && y == N - 1) {
        answer = min(answer, cost);
        return;
    }

    for (int i = 0; i < 4; i++) {
        int nx = x + dirs[i];
        int ny = y + dirs[i + 1];

        if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
        if (board[nx][ny] == 1) continue;

        int ncost;
        if (dir == -1 || dir == i) ncost = cost + 100;
        else ncost = cost + 600;

        if (dist[nx][ny][i] < ncost) continue;
        dist[nx][ny][i] = ncost;

        dfs(nx, ny, i, ncost, board, dist);
    }
}

int solution(vector<vector<int>> board) {
    N = board.size();
    vector<vector<vector<int>>> dist(N, vector<vector<int>>(N, vector<int>(4, 1e9)));

    dfs(0, 0, -1, 0, board, dist);

    return answer;
}
