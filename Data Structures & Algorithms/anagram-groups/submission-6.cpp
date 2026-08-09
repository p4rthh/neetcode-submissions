using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> final;
        for (auto x : strs) {
            string key = x;
            sort(key.begin(), key.end());
            final[key].push_back(x);
        }
        vector<vector<string>> values;
        for (auto x: final) {
            values.push_back(x.second);
        }
        return values;
    }
};
