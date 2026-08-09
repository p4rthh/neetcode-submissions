class Solution:
    def frequencyArray(self, string: str) -> List[int]:
        return vec
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = dict()
        for i in strs:
            vec = [0]*26
            for j in i:
                index = ord(j) - ord('a')
                vec[index] += 1
            key = tuple(vec)
            if key in final.keys():
                final[key].append(i)
            else:
                final[key] = [i]
        return list(final.values())
