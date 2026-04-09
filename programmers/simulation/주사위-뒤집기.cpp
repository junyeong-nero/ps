#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>

using namespace std;

int N; 

map<int,int> func(vector<vector<int>>& dice, set<int> dice_indices) {
    map<int,int> d;
    d[0] = 1;
    
    for (auto index : dice_indices) {
        
        map<int,int> new_d;
        for (auto [num1, prob] : d)
            for (auto num2 : dice[index])
                new_d[num1 + num2] += prob;
        
        d = new_d;
    }
    
    return d;
}

int func2(set<int> a_indices, vector<vector<int>>& dice) {
    
    set<int> b_indices;
    for (int i = 0; i < N; i++) b_indices.insert(i);
    for (int i : a_indices) b_indices.erase(i);
    
    map<int,int> prob_a = func(dice, a_indices);
    map<int,int> prob_b = func(dice, b_indices);
    
    int res = 0; 
    for (auto [num_a, count_a] : prob_a) {
        for (auto [num_b, count_b] : prob_b) {
            if (num_a > num_b)
                res += count_a * count_b;
        }
    }
    
    return res;
}


int max_prob = 0;
vector<int> max_indices;

void func3(int index, set<int> a_indices, vector<vector<int>>& dice) {
    
    if (a_indices.size() == N / 2) {
        
        for (int elem : a_indices)
            cout << elem << ", ";
        int prob = func2(a_indices, dice);
        cout << endl;
        cout << prob << endl;
        
        if (prob > max_prob) {
            max_prob = prob;
            
            vector<int> temp(a_indices.begin(), a_indices.end());
            for (int& elem : temp)
                elem += 1;
            max_indices = temp;
        }
        return;
    }
    
    if (index == N)
        return;
    
    func3(index + 1, a_indices, dice);
    a_indices.insert(index);
    func3(index + 1, a_indices, dice);
    a_indices.erase(index);
}


vector<int> solution(vector<vector<int>> dice) {
    
    N = dice.size();
    
    // T1
    // map<int,int> temp = func(dice, {0, 1});
    // for (auto [key, value] : temp)
    //     cout << key << ": " << value << endl;
    
    // T2 
    // int temp = func2({0, 1}, dice);
    // cout << temp << endl; 
    
    func3(0, {}, dice);
    return max_indices;
}
