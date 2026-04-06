#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <set>

using namespace std;

int solution(string message, vector<vector<int>> spoiler_ranges) {
    
    int n = message.size();
    int answer = 0;
    
    vector<pair<int,int>> words;
    
    int i = 0;
    while (i < n) {
        int j = i;
        while (j < n && message[j] != ' ') {
            j++;
        }
        words.push_back({i, j - 1});
        i = j + 1;
    }
    
    int m = words.size();
    int l = spoiler_ranges.size();
    
    vector<vector<int>> hidden(l);
    vector<bool> visible(m, true);
    
    for (int i = 0; i < m; i++) {
        int x = words[i].first;
        int y = words[i].second;
        
        for (int j = 0; j < l; j++) {
            int a = max(x, spoiler_ranges[j][0]);
            int b = min(y, spoiler_ranges[j][1]);
            if (a <= b) {
                hidden[j].push_back(i);
                visible[i] = false;
            }
        }
    }
    
    set<string> revealed;
    
    for (int i = 0; i < m; i++) {        
        if (visible[i]) {
            string t = message.substr(
                words[i].first, 
                words[i].second - words[i].first + 1
            );
//             cout << words[i].first << " " << words[i].second << " ";
//             cout << t << "\n";
            
            revealed.insert(t);
        }
    }
    
    for (int j = 0; j < l; j++) {
        
        for (auto index : hidden[j]) {
            int x = words[index].first;
            int y = words[index].second;
            string t = message.substr(x, y - x + 1);
            cout << t << "\n";
            
            if (revealed.count(t))
                continue;
            
            revealed.insert(t);
            answer++;
        }
    }
    
    return answer;
}
