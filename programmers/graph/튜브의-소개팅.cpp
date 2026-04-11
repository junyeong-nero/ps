#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(int m, int n, int s, vector<vector<int>> time_map) {
    const long long INF = (long long)4e18;
    const int MAXD = m * n - 1;  // 단순 경로 최대 이동 횟수

    vector<vector<long long>> prev(m, vector<long long>(n, INF));
    vector<vector<long long>> cur(m, vector<long long>(n, INF));

    prev[0][0] = 0;

    // 시작점이 곧 도착점인 경우는 문제상 없음 (m,n >= 2)
    int dirs[5] = {1, 0, -1, 0, 1};

    for (int d = 0; d < MAXD; d++) {
        for (int i = 0; i < m; i++) {
            fill(cur[i].begin(), cur[i].end(), INF);
        }

        for (int x = 0; x < m; x++) {
            for (int y = 0; y < n; y++) {
                if (prev[x][y] == INF) continue;
                if (prev[x][y] > s) continue;

                for (int k = 0; k < 4; k++) {
                    int nx = x + dirs[k];
                    int ny = y + dirs[k + 1];

                    if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                    if (time_map[nx][ny] == -1) continue;

                    long long ntalk = prev[x][y] + (long long)time_map[nx][ny];
                    if (ntalk < cur[nx][ny]) {
                        cur[nx][ny] = ntalk;
                    }
                }
            }
        }

        if (cur[m - 1][n - 1] <= s) {
            return {d + 1, (int)cur[m - 1][n - 1]};
        }

        prev.swap(cur);
    }

    return {-1, -1};
}
