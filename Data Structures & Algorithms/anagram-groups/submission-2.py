class Solution:
    def frequencyArray(self, string: str) -> List[int]:
        vec = [0]*26
        for i in string:
            index = ord(i) - ord('a')
            vec[index] += 1
        return vec
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = dict()
        for i in strs:
            key = tuple(self.frequencyArray(i))
            if key in final.keys():
                final[key].append(i)
            else:
                final[key] = [i]
        return list(final.values())
