#include <string>
#include <vector>
#include <cmath>

using namespace std;

string solution(int n, int m, int x, int y, int r, int c, int k) {
    int dist = abs(x - r) + abs(y - c);

    if (dist > k || (k - dist) % 2 != 0)
        return "impossible";

    string answer = "";

    int dx[4] = {1, 0, 0, -1};
    int dy[4] = {0, -1, 1, 0};
    char dir[4] = {'d', 'l', 'r', 'u'};

    for (int step = 0; step < k; step++) {
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 1 || nx > n || ny < 1 || ny > m)
                continue;

            int remain = k - step - 1;
            int d = abs(nx - r) + abs(ny - c);

            if (d <= remain && (remain - d) % 2 == 0) {
                answer += dir[i];
                x = nx;
                y = ny;
                break;
            }
        }
    }

    return answer;
}
