#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    int n = numbers.size();
    
    queue<pair<int, int>> q;
    q.push({0, 0});
    
    while (!q.empty()) {
        auto& [index, cur] = q.front();
        q.pop();
        
        if (index == n){
            if (cur == target) {
                answer += 1;
            }
            continue;
        }
            
        q.push({index + 1, cur + numbers[index]});
        q.push({index + 1, cur - numbers[index]});
    }
    
    return answer;
}
