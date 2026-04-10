#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool check(pair<int,int> start, pair<int,int> end, vector<string>& board) {
    int dx = end.first - start.first;
    int dy = end.second - start.second;
    if (dx > 0) dx = 1;
    if (dx < 0) dx = -1;
    if (dy > 0) dy = 1;
    if (dy < 0) dy = -1;
    
    int x = start.first, y = start.second;
    char c = board[x][y];
        
    while (x != end.first || y != end.second) {
        x += dx;
        y += dy;
        if (board[x][y] == '*')
            return false;
        if (board[x][y] != '.' and board[x][y] != c)
            return false;
    }
    return x == end.first && y == end.second;
}

bool check_pair(vector<pair<int,int>>& arr, vector<string>& board) {
    if (arr.size() != 2)
        return false;
    
    int x1 = arr[0].first;
    int y1 = arr[0].second;
    int x2 = arr[1].first;
    int y2 = arr[1].second;
    
    pair<int,int> target1 = {x1, y2};
    pair<int,int> target2 = {x2, y1};
    
    bool a1 = check(arr[0], target1, board);
    bool b1 = check(arr[1], target1, board);
    bool a2 = check(arr[0], target2, board);
    bool b2 = check(arr[1], target2, board);
    
//     cout << a1 << b1 << endl;
//     cout << a2 << b2 << endl;
    
    if (a1 && b1)
        return true;
    if (a2 && b2)
        return true;
    
    return false;
}

string func(vector<vector<pair<int,int>>>& d, vector<string>& board) {
    string res = ""; 
    for (int i = 0; i < 26; i++) {
        if (check_pair(d[i], board)) {
            board[d[i][0].first][d[i][0].second] = '.';
            board[d[i][1].first][d[i][1].second] = '.';
            d[i].clear();
            res += (i + 'A');
            break;
        }
    }
    return res;
}


// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
string solution(int m, int n, vector<string> board) {
    
    // 1. 타일끼리 위치 먼저 확인
    // 2. 타일끼리 주어진 조건으로 연결 가능한지 확인
    // 3. 반복하면서 제거.
    vector<vector<pair<int,int>>> d(26);
    int tile_count = 0;
    
    for (int x = 0; x < m; x++) {
        for (int y = 0; y < n; y++) {
            char c = board[x][y];
            if (c != '.' && c != '*') {
                d[c - 'A'].push_back({x, y});
            }
        }
    }
    
    for (int i = 0; i < 26; i++)
        if (d[i].size() == 2)
            tile_count++;
    
    string res = "";
    while (true) {
        string temp = func(d, board);
        if (temp.empty())
            break;
        res += temp;
    }
    
    if (res.size() == tile_count)
        return res;
    
    return "IMPOSSIBLE";
}
