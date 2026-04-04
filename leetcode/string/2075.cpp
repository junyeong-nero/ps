#include <iostream>
using namespace std;

class Solution {
public:
    string decodeCiphertext(string encodedText, int rows) {
        int m = rows, n = encodedText.size() / rows;
        cout << m << " " << n;

        string s = "";

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int pos = j * n + i + j;
                if (pos >= encodedText.size())
                    break;
                s += encodedText[pos];
            }
        }

        while (!s.empty() && s.back() == ' ') {
            s.pop_back();
        }

        return s;
    }
};
