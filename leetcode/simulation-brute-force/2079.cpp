class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        
        int n = plants.size();

        int bucket = capacity;
        int current = -1;
        int index = 0;
        int steps = 0;

        while (index < n) {
            if (plants[index] <= bucket) {
                bucket -= plants[index];
                steps += (index - current);
                current = index;
                index++;
            } else {
                bucket = capacity;
                steps += (current + 1);
                current = -1;
            }
        }

        // if (current != -1)
        //     steps += (current + 1);

        return steps;
    }
};
