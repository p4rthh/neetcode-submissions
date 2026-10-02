class Solution {
public:
    bool isMatch(char p1, char p2) {
        if (p1 == '(' && p2 == ')') return true;
        if (p1 == '{' && p2 == '}') return true;
        if (p1 == '[' && p2 == ']') return true;
        return false;
    }

    bool isValid(string s) {
        stack<char> st;
        for (char ch: s) {
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            } else {
                if (!st.empty()) {
                    char topchar = st.top();
                    st.pop();
                    if (!isMatch(topchar, ch)) {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        if (st.empty()) {
            return true;
        }
        return false;
    }
};
