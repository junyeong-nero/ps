class MyCalendar {
public:

    set<pair<int,int>> d;

    MyCalendar() {

    }

    bool check_intersect(int x, int y, int start, int end) {
        int a = max(x, start);
        int b = min(y, end);
        return a < b;
    }
    
    bool book(int startTime, int endTime) {
        for (auto [x, y] : this->d) {
            bool temp = check_intersect(x, y, startTime, endTime);
            if (temp)
                return false;
        }

        d.insert({startTime, endTime});
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(startTime,endTime);
 */
