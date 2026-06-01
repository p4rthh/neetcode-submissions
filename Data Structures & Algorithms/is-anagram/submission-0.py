class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = dict()
        t_ = dict()
        for i in sorted(s):
            if i in s_.keys():
                s_[i] += 1
            else:
                s_[i] = 1
        for j in sorted(t):
            if j in t_.keys():
                t_[j] += 1
            else:
                t_[j] = 1
        if s_ == t_:
            return True
        return False