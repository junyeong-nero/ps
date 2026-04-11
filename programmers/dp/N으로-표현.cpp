#include <string>
#include <vector>
#include <iostream>
#include <set>
#include <map>

using namespace std;

int INF = 1e9;

int solution(int N, int number) {
    
    map<int, int> d;
    
    int base = 1;
    int cur = 0;
    for (int i = 1; i <= 8; i++) {
        cur += base;
        base *= 10;
        d[cur * N] = i;
    }
    
    for (int i = 1; i <= 8; i++) {
        
        map<int, int> new_d(d.begin(), d.end());
        
        for (auto [elem1, step1] : d) {
            for (auto [elem2, step2] : d) {
                
                if (step1 + step2 > 8)
                    continue;
                
                new_d[elem1 + elem2] = min(new_d[elem1 + elem2] == 0 ? INF : new_d[elem1 + elem2], step1 + step2);
                new_d[elem1 - elem2] = min(new_d[elem1 - elem2] == 0 ? INF : new_d[elem1 - elem2], step1 + step2);
                new_d[elem1 * elem2] = min(new_d[elem1 * elem2] == 0 ? INF : new_d[elem1 * elem2], step1 + step2);
                
                if (elem2 == 0)
                    continue;
                
                new_d[elem1 / elem2] = min(new_d[elem1 / elem2] == 0 ? INF : new_d[elem1 / elem2], step1 + step2);
            }
        }
        
        d = new_d;
        if (d.count(number))
            return d[number];
    }
    
    return -1;
}
