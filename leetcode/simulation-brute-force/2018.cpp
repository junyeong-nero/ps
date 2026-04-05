class Solution {
public:
    int m, n;

    bool check(vector<vector<char>>& board, int x, int y, string word) {
        int dirs[] = {1, 0, -1, 0, 1};

        for (int i = 0; i < 4; i++) {
            int dx = dirs[i], dy = dirs[i + 1];

            // 시작 직전 칸이 # 또는 보드 밖이어야 함
            int px = x - dx, py = y - dy;
            if (0 <= px && px < m && 0 <= py && py < n && board[px][py] != '#')
                continue;

            int nx = x, ny = y;
            int index = 0;

            while (index < word.size()) {
                if (nx < 0 || nx >= m || ny < 0 || ny >= n)
                    break;
                if (board[nx][ny] == '#')
                    break;
                if (board[nx][ny] != ' ' && board[nx][ny] != word[index])
                    break;

                nx += dx;
                ny += dy;
                index++;
            }

            if (index != word.size())
                continue;

            // 끝 다음 칸이 # 또는 보드 밖이어야 함
            if (0 <= nx && nx < m && 0 <= ny && ny < n && board[nx][ny] != '#')
                continue;

            return true;
        }

        return false;
    }

    bool placeWordInCrossword(vector<vector<char>>& board, string word) {
        m = board.size();
        n = board[0].size();

        string reverse_word = word;
        reverse(reverse_word.begin(), reverse_word.end());

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (check(board, i, j, word))
                    return true;
                if (check(board, i, j, reverse_word))
                    return true;
            }
        }

        return false;
    }
};
