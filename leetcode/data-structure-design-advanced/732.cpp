class MyCalendarThree {
public:

    map<int, int> d;

    MyCalendarThree() {
        
    }
    
    int book(int startTime, int endTime) {
        d[startTime]++;
        d[endTime]--;

        int k = 0, cur = 0;
        for (auto [time, value] : this->d) {
            cur += value;
            k = max(k, cur);
        }

        return k;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(startTime,endTime);
 */
