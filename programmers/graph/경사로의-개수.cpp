#include <bits/stdc++.h>
using namespace std;

int N, M;
const long long MOD = 1'000'000'007LL;
int dirs[] = {1, 0, -1, 0, 1};

bool inbound(int x, int y) {
    return 0 <= x && x < N && 0 <= y && y < M;
}

int key(int x, int y) {
    return x * M + y;
}

vector<long long> getTransitionsFrom(int sx, int sy,
                                     const vector<vector<int>>& grid,
                                     const vector<int>& d) {
    int S = N * M;
    vector<long long> cur(S, 0), nxt(S, 0);
    cur[key(sx, sy)] = 1;

    for (int step = 0; step < (int)d.size(); step++) {
        fill(nxt.begin(), nxt.end(), 0);

        for (int x = 0; x < N; x++) {
            for (int y = 0; y < M; y++) {
                int u = key(x, y);
                if (cur[u] == 0) continue;

                for (int dir = 0; dir < 4; dir++) {
                    int nx = x + dirs[dir];
                    int ny = y + dirs[dir + 1];
                    if (!inbound(nx, ny)) continue;

                    if (grid[nx][ny] - grid[x][y] == d[step]) {
                        int v = key(nx, ny);
                        nxt[v] = (nxt[v] + cur[u]) % MOD;
                    }
                }
            }
        }
        cur.swap(nxt);
    }

    return cur;
}

vector<vector<long long>> matMul(const vector<vector<long long>>& A,
                                 const vector<vector<long long>>& B) {
    int S = A.size();
    vector<vector<long long>> C(S, vector<long long>(S, 0));

    for (int i = 0; i < S; i++) {
        for (int k = 0; k < S; k++) {
            if (A[i][k] == 0) continue;
            for (int j = 0; j < S; j++) {
                if (B[k][j] == 0) continue;
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    return C;
}

vector<long long> vecMul(const vector<long long>& v,
                         const vector<vector<long long>>& Mtx) {
    int S = v.size();
    vector<long long> res(S, 0);

    for (int i = 0; i < S; i++) {
        if (v[i] == 0) continue;
        for (int j = 0; j < S; j++) {
            if (Mtx[i][j] == 0) continue;
            res[j] = (res[j] + v[i] * Mtx[i][j]) % MOD;
        }
    }
    return res;
}

int solution(vector<vector<int>> grid, vector<int> d, int k) {
    N = grid.size();
    M = grid[0].size();
    int S = N * M;

    vector<vector<long long>> T(S, vector<long long>(S, 0));

    for (int x = 0; x < N; x++) {
        for (int y = 0; y < M; y++) {
            int s = key(x, y);
            T[s] = getTransitionsFrom(x, y, grid, d);
        }
    }

    vector<long long> A(S, 1); // 모든 시작점에서 1가지

    while (k > 0) {
        if (k & 1) A = vecMul(A, T);
        T = matMul(T, T);
        k >>= 1;
    }

    long long answer = 0;
    for (long long x : A) {
        answer = (answer + x) % MOD;
    }
    return (int)answer;
}
