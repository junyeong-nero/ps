#include <algorithm>
#include <deque>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int INF = 1e9;

vector<int> solution(int m, int n, int h, int w, vector<vector<int>> drops) {
    vector<vector<int>> grid(m, vector<int>(n, INF));

    for (int i = 0; i < (int)drops.size(); i++) {
        int x = drops[i][0];
        int y = drops[i][1];
        grid[x][y] = i + 1;
    }

    vector<vector<int>> rowMin(m, vector<int>(n - w + 1));

    for (int i = 0; i < m; i++) {
        deque<int> dq;
        for (int j = 0; j < n; j++) {
            while (!dq.empty() && grid[i][dq.back()] >= grid[i][j]) dq.pop_back();
            dq.push_back(j);

            while (!dq.empty() && dq.front() <= j - w) dq.pop_front();

            if (j >= w - 1) {
                rowMin[i][j - w + 1] = grid[i][dq.front()];
            }
        }
    }

    vector<vector<int>> rectMin(m - h + 1, vector<int>(n - w + 1));

    for (int j = 0; j < n - w + 1; j++) {
        deque<int> dq;
        for (int i = 0; i < m; i++) {
            while (!dq.empty() && rowMin[dq.back()][j] >= rowMin[i][j]) dq.pop_back();
            dq.push_back(i);

            while (!dq.empty() && dq.front() <= i - h) dq.pop_front();

            if (i >= h - 1) {
                rectMin[i - h + 1][j] = rowMin[dq.front()][j];
            }
        }
    }

    vector<int> answer = {0, 0};
    int best = -1;

    for (int i = 0; i <= m - h; i++) {
        for (int j = 0; j <= n - w; j++) {
            if (rectMin[i][j] > best) {
                best = rectMin[i][j];
                answer = {i, j};
            }
        }
    }

    return answer;
}