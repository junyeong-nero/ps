class Robot {
public:

    vector<tuple<int,int,string>> pos;
    int index;

    Robot(int w, int h) {
        
        this->index = 0;
        this->pos.push_back({0, 0, "South"});
        
        for (int x = 1; x < w; x++) {
            this->pos.push_back({x, 0, "East"});
        }
        for (int y = 1; y < h; y++) {
            this->pos.push_back({w - 1, y, "North"});
        }
        for (int x = w - 2; x >= 0; x--) {
            this->pos.push_back({x, h - 1, "West"});
        }
        for (int y = h - 2; y >= 1; y--) {
            this->pos.push_back({0, y, "South"});
        }
    }
    
    void step(int num) {
        this->index = this->index + num;
    }
    
    vector<int> getPos() {
        auto [x, y, dir] = this->pos[this->index % this->pos.size()];
        return {x, y};
    }
    
    string getDir() {
        if (this->index == 0)
            return "East";

        auto [x, y, dir] = this->pos[this->index % this->pos.size()];
        return dir;
    }
};

/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */
