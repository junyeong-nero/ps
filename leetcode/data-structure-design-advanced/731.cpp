class MyCalendarTwo {
public:

    set<pair<int,int>> single_book;
    set<pair<int,int>> double_book;

    MyCalendarTwo() {
        
    }
    
    pair<int,int> check_intersect(int x, int y, int start, int end) {
        int a = max(x, start);
        int b = min(y, end);
        if (a < b)
            return {a, b};
        return {-1, -1};
    }
    
    bool book(int startTime, int endTime) {

        for (auto [x, y] : this->double_book) {
            auto [a, b] = check_intersect(x, y, startTime, endTime);
            if (a >= 0 && b >= 0) {
                return false;
            }
        }

        for (auto [x, y] : this->single_book) {
            auto [a, b] = check_intersect(x, y, startTime, endTime);
            if (a >= 0 && b >= 0) {
                this->double_book.insert({a, b});
            }
        }
        
        single_book.insert({startTime, endTime});
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(startTime,endTime);
 */

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(startTime,endTime);
 */
