#include <string>
#include <vector>
#include <iostream>

using namespace std;

int M;
int N;

bool rotate(vector<vector<int>>& key) {
    vector<vector<int>> temp(M, vector<int>(M, 0));

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            temp[j][M - 1 - i] = key[i][j];
        }
    }

    key = temp;
    return true;
}

int check(int x, int y, vector<vector<int>>& key, vector<vector<int>>& lock) {
    int count = 0;

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            int nx = x + i;
            int ny = y + j;

            if (nx < 0 || ny < 0 || nx >= N || ny >= N)
                continue;

            if (key[i][j] == 1 && lock[nx][ny] == 1)
                return 0;

            if (key[i][j] == 1 && lock[nx][ny] == 0)
                count++;
        }
    }

    return count;
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    M = key.size();
    N = lock.size();

    int target = 0;
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
            if (lock[x][y] == 0)
                target++;
        }
    }

    if (target == 0)
        return true;

    for (int k = 0; k < 4; k++) {
        if (k > 0)
            rotate(key);

        for (int x = -M + 1; x < N; x++) {
            for (int y = -M + 1; y < N; y++) {
                int filled = check(x, y, key, lock);
                if (filled == target)
                    return true;
            }
        }
    }

    return false;
}
