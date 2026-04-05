#include <algorithm>
using namespace std;

long long answer;
int D, S;

void dfs(long long cur, long long used, long long split) {
    // 현재 레벨을 전부 리프로 두는 경우
    answer = max(answer, cur);

    long long remain = D - used;
    if (remain <= 0) return;

    // 이번 레벨 일부를 2분기로 확장하고 끝내는 경우
    if (split * 2 <= S) {
        long long x = min(cur, remain);
        answer = max(answer, cur + x);
    }

    // 이번 레벨 일부를 3분기로 확장하고 끝내는 경우
    if (split * 3 <= S) {
        long long x = min(cur, remain);
        answer = max(answer, cur + 2 * x);
    }

    // 이번 레벨 전체를 2분기로 확장하고 더 내려가는 경우
    if (used + cur <= D && split * 2 <= S) {
        dfs(cur * 2, used + cur, split * 2);
    }

    // 이번 레벨 전체를 3분기로 확장하고 더 내려가는 경우
    if (used + cur <= D && split * 3 <= S) {
        dfs(cur * 3, used + cur, split * 3);
    }
}

int solution(int dist_limit, int split_limit) {
    D = dist_limit;
    S = split_limit;
    answer = 1;  // 아무것도 확장 안 하면 루트의 자식 1개가 리프
    dfs(1, 0, 1);
    return (int)answer;
}