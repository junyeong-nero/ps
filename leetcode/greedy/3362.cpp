class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        // queries 의 조합으로 zero 가 아닌 elements 를 얼마나 없앨 수 있는지
        // 체크해야 함. prefix 느낌으로 확인은 할 수 잇는데, 이건 -1 체크만
        // 가능할 것 같고 얼마나 효율적으로 제거할 수 잇을지는 확인 못함. 이거
        // query 가 순서대로 가는거라면 그냥 가능할지도. 그러면 어떻게
        // 체크할지가 관건. 쿼리 한 번마다 n배열을 모두 업데이트 하는건 너무
        // 비효율적인데. SegmentTree 를 써야할 것 같기두 ... -> 아니었고.

        sort(queries.begin(), queries.end());
        priority_queue<int> available;
        // max-heap

        priority_queue<int, vector<int>, greater<int>> assigned;
        // min-heap
        
        int count = 0;

        for (int time = 0, k = 0; time < nums.size(); time++) {

            while (!assigned.empty() && assigned.top() < time)
                assigned.pop();

            while (k < queries.size() && queries[k][0] <= time)
                available.push(queries[k++][1]);
                
            while (assigned.size() < nums[time] && !available.empty() &&
                   available.top() >= time) {
                assigned.push(available.top());
                available.pop();
                count++;
            }
            if (assigned.size() < nums[time])
                return -1;
        }
        return queries.size() - count;
    }
};
