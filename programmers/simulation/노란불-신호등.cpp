#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

int solution(vector<vector<int>> signals) {
    int answer = 0;
    
    int length = 1;
    for (auto signal : signals) {
        int A = signal[0];
        int B = signal[1];
        int C = signal[2];
        
        int total = A + B + C;
        
        length = length * total / gcd(length, total);
    }
    
    cout << "length : " << length << "\n";
    
    vector<bool> d(length, true);
    
    for (auto signal : signals) {
        int A = signal[0];
        int B = signal[1];
        int C = signal[2];
        
        int total = A + B + C;
        
        for (int i = 0; i < d.size(); i++) {
            if (i % total < A)
                d[i] = false;
            if (A + B <= i % total)
                d[i] = false;
        }
    }
    
    for (int i = 0; i < d.size(); i++) {
        if (d[i])
            return i + 1;
    }
    
    return -1;
}
