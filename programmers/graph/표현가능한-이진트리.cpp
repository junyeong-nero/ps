#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string to_binary(long long n) {
    if (n == 0) return "0";

    string s;
    while (n > 0) {
        s += char('0' + (n % 2));
        n /= 2;
    }
    reverse(s.begin(), s.end());
    return s;
}

bool is_all_zero(const string& s) {
    for (char c : s) {
        if (c == '1') return false;
    }
    return true;
}

bool dfs(const string& s) {
    if (s.size() == 1) return true;

    int mid = s.size() / 2;
    string left = s.substr(0, mid);
    string right = s.substr(mid + 1);

    if (s[mid] == '0') {
        return is_all_zero(left) && is_all_zero(right);
    }

    return dfs(left) && dfs(right);
}

bool check(long long number) {
    string bin = to_binary(number);

    int nodes = 1;
    while (nodes < (int)bin.size()) {
        nodes = nodes * 2 + 1;
    }

    string padded(nodes - bin.size(), '0');
    padded += bin;

    return dfs(padded);
}

vector<int> solution(vector<long long> numbers) {
    vector<int> answer;
    for (auto num : numbers) {
        answer.push_back(check(num) ? 1 : 0);
    }
    return answer;
}
